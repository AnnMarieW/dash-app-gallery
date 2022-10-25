from dash import Dash, dcc, html, Input, Output, State, MATCH
import plotly.express as px
import dash_bootstrap_components as dbc

df = px.data.gapminder()
default_column_x = "year"
default_column_y = "gdpPercap"
options = ["lifeExp", "year", "pop", "gdpPercap"]

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    dbc.Row(
        dbc.Col(
            [
                html.H3("Pattern Matching Callbacks Demo"),
                dbc.InputGroup(
                    [
                        dcc.Dropdown(
                            options=df.country.unique(),
                            value="Canada",
                            id="pattern-match-country",
                            clearable=False,
                            style={"width": 300},
                        ),
                        dbc.Button(
                            "Add Chart", id="pattern-match-add-chart", n_clicks=0
                        ),
                    ],
                    className="mb-3",
                ),
                html.Div(id="pattern-match-container", children=[], className="mt-4"),
            ]
        )
    ),
    fluid=True,
)


def create_figure(column_x, column_y, country):
    chart_type = px.line if column_x == "year" else px.scatter
    return (
        chart_type(
            df.query("country == '{}'".format(country)),
            x=column_x,
            y=column_y,
        )
        .update_layout(
            title="{} {} vs {}".format(country, column_x, column_y),
            margin_l=10,
            margin_r=0,
            margin_b=30,
        )
        .update_xaxes(title_text="")
        .update_yaxes(title_text="")
    )


def make_card(n_clicks, country):
    return dbc.Card(
        [
            dbc.CardHeader(
                [
                    f"Figure {n_clicks + 1} ",
                    dbc.Button(
                        "X",
                        id={"type": "dynamic-delete", "index": n_clicks},
                        n_clicks=0,
                        color="secondary",
                    ),
                ],
                className="text-end",
            ),
            dcc.Graph(
                id={"type": "dynamic-output", "index": n_clicks},
                style={"height": 300},
                figure=create_figure(default_column_x, default_column_y, country),
            ),
            dcc.Dropdown(
                id={"type": "dynamic-dropdown-x", "index": n_clicks},
                options=options,
                value=default_column_x,
                clearable=False,
            ),
            dcc.Dropdown(
                id={"type": "dynamic-dropdown-y", "index": n_clicks},
                options=options,
                value=default_column_y,
                clearable=False,
            ),
        ],
        style={
            "width": 400,
            "display": "inline-block",
        },
        className="m-1",
        id={"type": "dynamic-card", "index": n_clicks},
    )


@app.callback(
    Output("pattern-match-container", "children"),
    Input("pattern-match-add-chart", "n_clicks"),
    State("pattern-match-container", "children"),
    State("pattern-match-country", "value"),
)
def add_card(n_clicks, cards, country):
    new_card = make_card(n_clicks, country)
    cards.append(new_card)
    return cards


@app.callback(
    Output({"type": "dynamic-card", "index": MATCH}, "style"),
    Input({"type": "dynamic-delete", "index": MATCH}, "n_clicks"),
    prevent_initial_call=True,
)
def remove_card(_):
    return {"display": "none"}


@app.callback(
    Output({"type": "dynamic-output", "index": MATCH}, "figure"),
    Input({"type": "dynamic-dropdown-x", "index": MATCH}, "value"),
    Input({"type": "dynamic-dropdown-y", "index": MATCH}, "value"),
    Input("pattern-match-country", "value"),
)
def update_figure(column_x, column_y, country):
    return create_figure(column_x, column_y, country)


if __name__ == "__main__":
    app.run_server(debug=True)
