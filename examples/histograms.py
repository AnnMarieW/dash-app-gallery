from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import numpy as np

app = Dash(__name__)


app.layout = html.Div(
    [
        html.H4("Interactive normal distribution"),
        dcc.Graph(id="histograms-x-graph"),
        html.P("Mean:"),
        dcc.Slider(
            id="histograms-x-mean", min=-3, max=3, value=0, marks={-3: "-3", 3: "3"}
        ),
        html.P("Standard Deviation:"),
        dcc.Slider(
            id="histograms-x-std", min=1, max=3, value=1, marks={1: "1", 3: "3"}
        ),
    ]
)


@app.callback(
    Output("histograms-x-graph", "figure"),
    Input("histograms-x-mean", "value"),
    Input("histograms-x-std", "value"),
)
def display_color(mean, std):
    data = np.random.normal(mean, std, size=500)
    fig = px.histogram(data, range_x=[-10, 10])
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
