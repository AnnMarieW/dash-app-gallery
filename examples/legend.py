from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = px.data.gapminder().query("year==2007")

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Interactive legend position with Dash"),
        html.P("Select legend position:"),
        dcc.RadioItems(
            id="legend-x-xanchor",
            value=0,
            inline=True,
            options=[{"label": "left", "value": 0}, {"label": "right", "value": 1}],
        ),
        dcc.RadioItems(
            id="legend-x-yanchor",
            value=1,
            inline=True,
            options=[{"label": "top", "value": 1}, {"label": "bottom", "value": 0}],
        ),
        dcc.Graph(id="legend-x-graph"),
    ]
)


@app.callback(
    Output("legend-x-graph", "figure"),
    Input("legend-x-xanchor", "value"),
    Input("legend-x-yanchor", "value"),
)
def modify_legend(pos_x, pos_y):
    fig = px.scatter(
        df,
        x="gdpPercap",
        y="lifeExp",
        color="continent",
        size="pop",
        size_max=45,
        log_x=True,
    )
    fig.update_layout(legend_x=pos_x, legend_y=pos_y)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
