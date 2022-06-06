from dash import Dash, dcc, html
from plotly import data
import plotly.express as px

# Tab 1
gapminder = data.gapminder()
fig_gapminder = px.scatter(
    gapminder.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

# Tab 2
iris = data.iris()
fig_iris = px.scatter(iris, x="sepal_length", y="sepal_width", color="species")

# App
app = Dash(__name__)
app.layout = html.Div(
    [
        dcc.Tabs(
            [
                dcc.Tab(label="Iris", children=[dcc.Graph(figure=fig_iris)]),
                dcc.Tab(label="Gapminder", children=[dcc.Graph(figure=fig_gapminder)]),
            ]
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
