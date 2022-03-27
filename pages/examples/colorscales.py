from dash import Dash, dcc, html, Input, Output
import plotly.express as px

colorscales = px.colors.named_colorscales()

app = Dash(__name__)


app.layout = html.Div(
    [
        html.H4("Interactive color scale"),
        html.P("Select your palette:"),
        dcc.Dropdown(id="colorscales-x-dropdown", options=colorscales, value="viridis"),
        dcc.Graph(id="colorscales-x-graph"),
    ]
)


@app.callback(
    Output("colorscales-x-graph", "figure"), Input("colorscales-x-dropdown", "value")
)
def change_colorscale(scale):
    df = px.data.iris()  # replace with your own data source
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
