from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = px.data.iris()

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Iris plot an interactive horizontal line"),
        dcc.Graph(id="horizontal-vertical-shapes-x-graph"),
        html.P("Position of hline"),
        dcc.Slider(
            id="horizontal-vertical-shapes-x-slider-position",
            min=1,
            max=7,
            value=2.5,
            step=0.1,
            marks={1: "1", 7: "7"},
        ),
    ]
)


@app.callback(
    Output("horizontal-vertical-shapes-x-graph", "figure"),
    Input("horizontal-vertical-shapes-x-slider-position", "value"),
)
def display_graph(pos_x):
    fig = px.scatter(df, x="petal_length", y="petal_width")
    fig.add_vline(x=pos_x, line_width=3, line_dash="dash", line_color="green")
    fig.add_hrect(y0=0.9, y1=2.6, line_width=0, fillcolor="red", opacity=0.2)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
