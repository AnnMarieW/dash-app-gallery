from dash import Dash, html, dcc, Input, Output
import dash_daq as daq
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/auto-mpg.csv"
)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

gauge = html.Div(
    [
        daq.Gauge(
            label="Acceleration",
            scale={"start": 0, "interval": 2, "labelInterval": 2},
            id="gauge-scatterplot-x-gauge",
            showCurrentValue=True,
            units="MPH/s",
            min=0,
            max=20,
            value=12,
        ),
        dcc.Slider(id="gauge-scatterplot-x-slider", min=12, max=18, step=1, value=12),
    ],
    className="d-grid gap-2",
)

app.layout = dbc.Container(
    [
        html.H2("Filtering Car Acceleration with Gauge"),
        dbc.Row(
            [
                dbc.Col([gauge], md=4),
                dbc.Col(dcc.Graph(id="gauge-scatterplot-x-graph"), md=8),
            ],
            align="center",
        ),
    ]
)


@app.callback(
    Output("gauge-scatterplot-x-gauge", "value"),
    Input("gauge-scatterplot-x-slider", "value"),
)
def update_output(value):
    return value


@app.callback(
    Output("gauge-scatterplot-x-graph", "figure"),
    Input("gauge-scatterplot-x-slider", "value"),
)
def update_graph(value):
    fig = px.scatter(
        df.query(f"acceleration=={value}"),
        x="weight",
        y="mpg",
        height=500,
        title="MPG vs Weight of Cars",
    )
    fig.update(layout=dict(title=dict(x=0.5)))
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
