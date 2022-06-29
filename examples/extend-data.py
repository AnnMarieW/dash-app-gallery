import numpy as np
from dash import Dash, html, dcc, Input, Output, State, clientside_callback

# Example from https://stackoverflow.com/a/63681810/2428887
resolution = 1000
t = np.linspace(0, np.pi * 2, resolution)
x, y = np.cos(t), np.sin(t)  # example data (a circle)
figure = dict(
    data=[{"x": [], "y": []}],
    layout=dict(xaxis=dict(range=[-1, 1]), yaxis=dict(range=[-1, 1])),
)
app = Dash(__name__, update_title=None)  # remove "Updating..." from title
app.layout = html.Div(
    [
        html.H4("Smooth updates using clientside callbacks"),
        dcc.Graph(id="extend-data-x-graph", figure=dict(figure)),
        dcc.Interval(id="extend-data-x-interval", interval=25, max_intervals=200),
        dcc.Store(id="extend-data-x-offset", data=0),
        dcc.Store(id="extend-data-x-store", data=dict(x=x, y=y, resolution=resolution)),
    ]
)
clientside_callback(
    """
    function (n_intervals, data, offset) {
        offset = offset % data.x.length;
        const end = Math.min((offset + 10), data.x.length);
        return [[{x: [data.x.slice(offset, end)], y: [data.y.slice(offset, end)]}, [0], 500], end]
    }
    """,
    [
        Output("extend-data-x-graph", "extendData"),
        Output("extend-data-x-offset", "data"),
    ],
    [Input("extend-data-x-interval", "n_intervals")],
    [State("extend-data-x-store", "data"), State("extend-data-x-offset", "data")],
)

if __name__ == "__main__":
    app.run_server()
