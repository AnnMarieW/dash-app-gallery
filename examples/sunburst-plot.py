from dash import Dash, Input, Output, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import numpy as np

df = px.data.gapminder()

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    dbc.Row(
        [
            dbc.Col(
                [
                    html.Label("Select year:"),
                    dcc.Dropdown(
                        id="sunburst-plot-x-year",
                        options=df.year.unique(),
                        value=1992,
                        clearable=False,
                    ),
                ],
                width=3,
            ),
            dbc.Col(
                [dcc.Graph(id="sunburst-plot-x-graph")],
                width=9,
            ),
        ]
    )
)


@app.callback(
    Output("sunburst-plot-x-graph", "figure"), Input("sunburst-plot-x-year", "value")
)
def generate_graph(year):
    dff = px.data.gapminder().query(f"year == {year}")
    fig = px.sunburst(
        dff,
        path=["continent", "country"],
        values="pop",
        color="lifeExp",
        hover_data=["iso_alpha"],
        color_continuous_scale="RdBu",
        color_continuous_midpoint=np.average(df["lifeExp"], weights=df["pop"]),
    )

    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
