from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/Emissions%20Data.csv"
)
df = df.query("Year == 2011")

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

bar_slider = html.Div(
    [

       dcc.Slider(
            id="graduated-bar-filter-x-slider",
            min=0,
            max=10,
            value=5,
        ),
    ]
)

app.layout = dbc.Container(
    [
        html.H2("Filtering a Bar Chart with a Slider"),
        dbc.Row(
            [
                dbc.Col(bar_slider, md=4),
                dbc.Col(dcc.Graph(id="graduated-bar-filter-x-graph"), md=8),
            ],
            align="center",
        ),
    ]
)


@app.callback(
    Output("graduated-bar-filter-x-graph", "figure"),
    Input("graduated-bar-filter-x-slider", "value"),
)
def update_graph(value):
    dff = df.loc[df["Emission"] > value]
    fig = px.bar(
        dff,
        x="Country",
        y="Emission",
        title="Countries with Highest Emission Levels in 2011",
    )
    fig.update(layout=dict(title=dict(x=0.5)))
    return fig


if __name__ == "__main__":
    app.run(debug=True)
