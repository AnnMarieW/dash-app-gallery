from dash import Dash, dcc, html, Input, Output, State, ALL, MATCH, ctx
import plotly.express as px
import dash_bootstrap_components as dbc

df = px.data.gapminder()
default_column_x = "year"
default_column_y = "gdpPercap"

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(html.H3("Pattern Matching Callbacks Demo"))),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(
                        options=df.country.unique(),
                        value="Canada",
                        id="pattern-match-x-country",
                    ),
                    width=4,
                ),
                dbc.Col(
                    dbc.Button(
                        "Add Chart",
                        id="pattern-match-x-add-chart",
                        n_clicks=0,
                    )
                ),
            ]
        ),
        dbc.Row(dbc.Col(id="pattern-match-x-container", children=[], className="mt-4")),
    ],
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


@app.callback(
    Output("pattern-match-x-container", "children"),
    Input("pattern-match-x-add-chart", "n_clicks"),
    Input({"type": "dynamic-delete", "index": ALL}, "n_clicks"),
    State("pattern-match-x-container", "children"),
    State("pattern-match-x-country", "value"),
)
def display_dropdowns(n_clicks, _, children, country):
    triggered = ctx.triggered_id
    if isinstance(triggered, dict):
        delete_chart_number = triggered["index"]
        children = [
            chart
            for chart in children
            if "'index': " + str(delete_chart_number) not in str(chart)
        ]
    else:
        new_element = dbc.Card(
            [
                dbc.CardHeader(
                    [
                        f"Figure {n_clicks+1} ",
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
                    options=df.columns,
                    value=default_column_x,
                ),
                dcc.Dropdown(
                    id={"type": "dynamic-dropdown-y", "index": n_clicks},
                    options=df.columns,
                    value=default_column_y,
                ),
            ],
            style={
                "width": 400,
                "display": "inline-block",
            },
            className="m-1",
        )
        children.append(new_element)
    return children


@app.callback(
    Output({"type": "dynamic-output", "index": MATCH}, "figure"),
    Input({"type": "dynamic-dropdown-x", "index": MATCH}, "value"),
    Input({"type": "dynamic-dropdown-y", "index": MATCH}, "value"),
    Input("pattern-match-x-country", "value"),
)
def display_output(column_x, column_y, country):
    return create_figure(column_x, column_y, country)


if __name__ == "__main__":
    app.run_server(debug=True)
