from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Country's key performance analytics"),
        html.P("Select data on y-axis:"),
        dcc.Dropdown(
            id="filled-area-plots-x-y-axis",
            options=["lifeExp", "pop", "gdpPercap"],
            value="gdpPercap",
        ),
        dcc.Graph(id="filled-area-plots-x-graph"),
    ]
)


@app.callback(
    Output("filled-area-plots-x-graph", "figure"),
    Input("filled-area-plots-x-y-axis", "value"),
)
def display_area(y):
    df = px.data.gapminder()  # replace with your own data source
    countries = df.country.drop_duplicates().sample(n=10, random_state=42)
    df = df[df.country.isin(countries)]

    fig = px.area(df, x="year", y=y, color="continent", line_group="country")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
