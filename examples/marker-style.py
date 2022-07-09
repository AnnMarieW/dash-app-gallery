from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import plotly.express as px
import dash_daq as daq

df = px.data.iris()

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Interactive marker style control"),
        dcc.Graph(id="marker-style-x-graph"),
        daq.ColorPicker(
            id="marker-style-x-color",
            label="Border Color",
            value=dict(hex="#2F4F4F"),
            size=164,
        ),
    ]
)


@app.callback(
    Output("marker-style-x-graph", "figure"), Input("marker-style-x-color", "value")
)
def update_marker_border(color):
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", height=350)
    fig = go.Figure(fig)
    fig.update_traces(
        marker_size=12,
        marker_line=dict(width=2, color=color["hex"]),
        selector=dict(mode="markers"),
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
