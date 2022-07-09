from dash import Dash, dcc, html, Input, Output
import plotly.express as px

colorscales = px.colors.named_colorscales()
df = px.data.iris()

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Interactive Plotly Express color scale selection"),
        html.P("Color Scale"),
        dcc.Dropdown(
            id="builtin-colorscales-x-dropdown", options=colorscales, value="viridis"
        ),
        dcc.Graph(id="builtin-colorscales-x-graph"),
    ]
)


@app.callback(
    Output("builtin-colorscales-x-graph", "figure"),
    Input("builtin-colorscales-x-dropdown", "value"),
)
def change_colorscale(scale):
    fig = px.scatter(
        df,
        x="sepal_width",
        y="sepal_length",
        color="sepal_length",
        color_continuous_scale=scale,
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
