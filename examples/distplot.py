from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = px.data.tips()

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Analysis of the restaurant's revenue"),
        html.P("Select Distribution:"),
        dcc.RadioItems(
            id="distplot-x-distribution",
            options=["box", "violin", "rug"],
            value="box",
            inline=True,
        ),
        dcc.Graph(id="distplot-x-graph"),
    ]
)


@app.callback(
    Output("distplot-x-graph", "figure"), Input("distplot-x-distribution", "value")
)
def display_graph(distribution):
    fig = px.histogram(
        df,
        x="total_bill",
        y="tip",
        color="sex",
        marginal=distribution,
        range_x=[-5, 60],
        hover_data=df.columns,
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
