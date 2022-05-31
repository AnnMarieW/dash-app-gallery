from dash import Dash, html, dcc, Input, Output, State, MATCH, ALL
import json
import requests

app = Dash(__name__)

questionnaire = requests.get(
    "https://raw.githubusercontent.com/IcToxi/datasets/main/questionnaire.json"
).json()


def generate(k, v):
    _id = {
        "category": "questionnaire",
        "index": k,
        "type": v["type"],
        "additional": False,
    }

    question = html.P(k + ". " + v["question"])
    options = {i: i for i in v["options"]} if "options" in v else None

    match v["type"]:
        case "choice":
            return html.Div([question, dcc.RadioItems(id=_id, options=options)])
        case "multi-choice":
            return html.Div([question, dcc.Checklist(id=_id, options=options)])
        case "choice+blank":
            return html.Div(
                [
                    question,
                    dcc.RadioItems(id=_id, options=options),
                    dcc.Input(id=_id | {"additional": True}, disabled=True),
                ]
            )
        case "blank":
            return html.Div([question, dcc.Input(id=_id)])
        case "essay":
            return html.Div([question, dcc.Textarea(id=_id)])
        case _:
            return html.Div("Something is wrong...")


app.layout = html.Div(
    [generate(k, v) for k, v in questionnaire.items()]
    + [html.Br(), btn := html.Button("Submit"), answers := html.Pre()]
)


app.clientside_callback(
    "(v => v === 'Yes' ? false : true)",
    Output(
        {
            "category": "questionnaire",
            "type": "choice+blank",
            "additional": True,
            "index": MATCH,
        },
        "disabled",
    ),
    Input(
        {
            "category": "questionnaire",
            "type": "choice+blank",
            "additional": False,
            "index": MATCH,
        },
        "value",
    ),
)


app.clientside_callback(
    "(answers => answers.every(Boolean) ? false : true)",
    Output(btn, "disabled"),
    Input(
        {"category": "questionnaire", "type": ALL, "additional": False, "index": ALL},
        "value",
    ),
)


@app.callback(
    Output(answers, "children"),
    Input(btn, "n_clicks"),
    [
        State(
            {"category": "questionnaire", "type": ALL, "additional": ALL, "index": ALL},
            "id",
        ),
        State(
            {"category": "questionnaire", "type": ALL, "additional": ALL, "index": ALL},
            "value",
        ),
    ],
    prevent_initial_call=True,
)
def collect(n_clicks, index, answer):
    return json.dumps(
        {"answers": [v | {"answer": answer[i]} for i, v in enumerate(index)]}, indent=2
    )


if __name__ == "__main__":
    app.run_server(debug=True)
