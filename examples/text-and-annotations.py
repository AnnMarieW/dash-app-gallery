from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = px.data.gapminder().query("year==2007")

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Live control of annotations"),
        html.P("Select text position:"),
        dcc.RadioItems(
            id="text-and-annotations-x-pos-x",
            inline=True,
            options=["left", "center", "right"],
            value="center",
        ),
        dcc.RadioItems(
            id="text-and-annotations-x-pos-y",
            inline=True,
            options=["top", "bottom"],
            value="top",
        ),
        dcc.Graph(id="text-and-annotations-x-graph"),
    ]
)


@app.callback(
    Output("text-and-annotations-x-graph", "figure"),
    Input("text-and-annotations-x-pos-x", "value"),
    Input("text-and-annotations-x-pos-y", "value"),
)
def modify_legend(pos_x, pos_y):
    fig = px.scatter(
        df,
        x="gdpPercap",
        y="lifeExp",
        text="country",
        log_x=True,
        size_max=60,
        title="GDP and Life Expectancy (Americas, 2007)",
    )
    fig.update_traces(textposition=f"{pos_y} {pos_x}")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
