from dash import Dash, dcc, html, Input, Output
import dash_daq as daq
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/Canada%20Immigration.csv"
)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        html.H2("Changing a Graph with Indicator & Button"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    daq.Indicator(
                        id="indicator-graph-x-indicator",
                        size=25,
                    ),
                    md=1,
                ),
                dbc.Col(
                    html.Button(
                        "Change Graph", id="indicator-graph-x-button", n_clicks=0
                    ),
                    md=2,
                ),
                dbc.Col(dcc.Graph(id="indicator-graph-x-graph"), md=9),
            ],
            align="center",
        ),
    ]
)


@app.callback(
    Output("indicator-graph-x-indicator", "value"),
    Input("indicator-graph-x-button", "n_clicks"),
)
def update_output(value):
    if value % 2 == 0:
        return True
    else:
        return False


@app.callback(
    Output("indicator-graph-x-graph", "figure"),
    Input("indicator-graph-x-indicator", "value"),
)
def update_graph(value):
    if value == True:
        return px.bar(
            df, x="Year", y="USA", title="Canadian Immigration Numbers from USA"
        )
    else:
        return px.line(
            df, x="Year", y="USA", title="Canadian Immigration Numbers from USA"
        )


if __name__ == "__main__":
    app.run_server(debug=True)
