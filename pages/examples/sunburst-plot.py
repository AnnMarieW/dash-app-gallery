import dash
from dash import Dash, Input, Output, State, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import numpy as np

df = px.data.gapminder().query("year >= 1992")

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], prevent_initial_callbacks=True)

app.layout = dbc.Container(
    dbc.Row(
        [
            dbc.Col(
                [
                    html.Label("Select year:"),
                    dcc.Dropdown(
                        id="sunburst-plot-x-year",
                        options=df.year.unique()
                    ),
                    html.Label("Select continent:"),
                    dcc.Dropdown(id="sunburst-plot-x-continent", multi=True),
                    html.Label("Select country:"),
                    dcc.Dropdown(id="sunburst-plot-x-country", multi=True)
                ],
                width=3,
            ),
            dbc.Col(
                [
                    dcc.Graph(id="sunburst-plot-x-graph")
                ],
                width=9,
            ),
        ]
    )
)


@app.callback(
    Output("sunburst-plot-x-continent", "options"),
    Input("sunburst-plot-x-year", "value"),
)
def chained_dropdown_1(year):
    if year is None:
        return []
    else:
        return df.query(f"year == {year}").continent.unique()


@app.callback(
    Output("sunburst-plot-x-country", "options"),
    Input("sunburst-plot-x-continent", "value"),
    Input("sunburst-plot-x-year", "value"),
)
def chained_dropdown_2(continent, year):
    if year is None:
        return []
    elif continent is None:
        return []
    else:
        return df.query(f"continent == {continent} & year == {year}").country.unique()


@app.callback(
    Output("sunburst-plot-x-graph", "figure"),
    Input("sunburst-plot-x-country", "value"),
    State("sunburst-plot-x-year", "value"),
    State("sunburst-plot-x-continent", "value"),
)
def generate_graph(country, year, continent):
    if len(country)==0:
        return {}
    else:
        dff = df.query(f"year == {year} & continent in {continent} & country in {country}")

        fig = px.sunburst(
            dff,
            path=["continent", "country"],
            values="pop",
            color="lifeExp",
            hover_data=["iso_alpha"],
            color_continuous_scale="RdBu",
            color_continuous_midpoint=np.average(dff["lifeExp"], weights=dff["pop"]),
        )

        fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
        return fig


if __name__ == "__main__":
    app.run_server(debug=True)
