from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = px.data.gapminder()

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Animated GDP and population over decades"),
        html.Label("Select an animation:", htmlFor="animations-x-selection"),
        dcc.RadioItems(
            id="animations-x-selection",
            options=["GDP - Scatter", "Population - Bar"],
            value="GDP - Scatter",
        ),
        dcc.Loading(dcc.Graph(id="animations-x-graph"), type="cube"),
    ]
)


@app.callback(
    Output("animations-x-graph", "figure"), Input("animations-x-selection", "value")
)
def display_animated_graph(selection):
    animations = {
        "GDP - Scatter": px.scatter(
            df,
            x="gdpPercap",
            y="lifeExp",
            animation_frame="year",
            animation_group="country",
            size="pop",
            color="continent",
            hover_name="country",
            log_x=True,
            size_max=55,
            range_x=[100, 100000],
            range_y=[25, 90],
        ),
        "Population - Bar": px.bar(
            df,
            x="continent",
            y="pop",
            color="continent",
            animation_frame="year",
            animation_group="country",
            range_y=[0, 4000000000],
        ),
    }
    return animations[selection]


if __name__ == "__main__":
    app.run_server(debug=True)
