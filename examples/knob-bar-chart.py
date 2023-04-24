from dash import Dash, html, dcc, Input, Output
import dash_daq as daq
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/spinrates.csv"
)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

knob = html.Div(
    [
        daq.Knob(
            id="knob-bar-chart-x-knob",
            label="Velocity",
            value=90,
            min=90,
            max=100,
            scale={"start": 90, "labelInterval": 2, "interval": 2},
        ),
        html.Div(id="knob-bar-chart-x-knob-output"),
    ],
)


app.layout = dbc.Container(
    [
        html.H2("Filtering a Bar Chart with Knob"),
        dbc.Row(
            [
                dbc.Col(knob, md=3),
                dbc.Col(dcc.Graph(id="knob-bar-chart-x-graph"), md=9),
            ],
            align="center",
        ),
    ]
)


@app.callback(
    Output("knob-bar-chart-x-knob-output", "children"),
    Input("knob-bar-chart-x-knob", "value"),
)
def update_output(value):
    return f"Filter the graph for velocity ≤ {value}"


@app.callback(
    Output("knob-bar-chart-x-graph", "figure"), Input("knob-bar-chart-x-knob", "value")
)
def update_graph(value):
    dff = df.loc[df["velocity"] <= value]
    fig = px.bar(dff, x="spinrate", y="swing_miss", title="Swing Miss vs Spin Rate")
    fig.update(layout=dict(title=dict(x=0.5)))
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
