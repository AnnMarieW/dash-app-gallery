from dash import Dash, html, dcc, Input, Output
import dash_daq as daq
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

df = px.data.tips()

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

gauge = html.Div(
    [
        daq.Gauge(
            label="Party Size",
            scale={"start": 0, "interval": 1, "labelInterval": 1},
            id="gauge-pie-chart-x-gauge",
            min=0,
            max=6,
            value=1,
        ),
        dcc.Slider(id="gauge-pie-chart-x-slider", min=1, max=6, step=1, value=1),
    ],
    className="d-grid gap-2",
)

app.layout = dbc.Container(
    [
        html.H2("Filtering Pie Chart Values with Gauge"),
        dbc.Row(
            [
                dbc.Col(gauge, md=6),
                dbc.Col(dcc.Graph(id="gauge-pie-chart-x-graph"), md=6),
            ],
            align="center",
        ),
    ]
)


@app.callback(
    Output("gauge-pie-chart-x-gauge", "value"),
    Input("gauge-pie-chart-x-slider", "value"),
)
def update_output(value):
    return value


@app.callback(
    Output("gauge-pie-chart-x-graph", "figure"),
    Input("gauge-pie-chart-x-slider", "value"),
)
def update_graph(value):
    dff = df.loc[df["size"] == value]
    fig = px.pie(dff, values="tip", names="day", title="Restaurant Tips")
    fig.update(layout=dict(title=dict(x=0.5)))
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
