from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = px.data.gapminder()

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Life expectancy progression of countries per continents"),
        dcc.Graph(id="line-charts-x-graph"),
        dcc.Checklist(
            id="line-charts-x-checklist",
            options=["Asia", "Europe", "Africa", "Americas", "Oceania"],
            value=["Americas", "Oceania"],
            inline=True,
        ),
    ]
)


@app.callback(
    Output("line-charts-x-graph", "figure"), Input("line-charts-x-checklist", "value")
)
def update_line_chart(continents):
    mask = df.continent.isin(continents)
    fig = px.line(df[mask], x="year", y="lifeExp", color="country")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
