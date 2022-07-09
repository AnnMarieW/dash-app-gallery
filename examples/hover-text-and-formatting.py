from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = px.data.gapminder().query("continent=='Oceania'")
app = Dash(__name__)


app.layout = html.Div(
    [
        html.H4("Life expectancy plot with a selectable hover mode"),
        html.P("Select hovermode:"),
        dcc.RadioItems(
            id="hover-text-and-formatting-x-hovermode",
            inline=True,
            options=["x", "x unified", "closest"],
            value="closest",
        ),
        dcc.Graph(id="hover-text-and-formatting-x-graph"),
    ]
)


@app.callback(
    Output("hover-text-and-formatting-x-graph", "figure"),
    Input("hover-text-and-formatting-x-hovermode", "value"),
)
def update_hovermode(mode):
    fig = px.line(
        df,
        x="year",
        y="lifeExp",
        color="country",
        title="Hover over points to see the change",
    )
    fig.update_traces(mode="markers+lines", hovertemplate=None)
    fig.update_layout(hovermode=mode)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
