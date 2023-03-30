from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import dash_daq as daq
import plotly.io as pio

df = px.data.gapminder()
df = df.loc[df['year']==1952]

pio.templates.default = "ggplot2"

app = Dash(__name__)

picker_style = {"display": "inline-block", "margin": 10}

app.layout = html.Div(
    [
        html.H2("Interactive Bar Colour Control"),
        dcc.Loading(dcc.Graph(id="graph"), type="circle"),
        daq.ColorPicker(
            id="color",
            label="Color of Bars",
            size=164,
            value=dict(hex="#564AE6")
        ),
    ]
)


@app.callback(
    Output("graph", "figure"), Input("color", "value"),
)


def update_points_color(color):
    fig = px.histogram(df, x='lifeExp',
                       labels={'lifeExp': "Life Expectancy (years)"},
                       title="Life Expectancy for Countries in 1952", nbins=23)
    fig = go.Figure(fig)
    fig.update_layout(yaxis_title="Number of Countries")
    fig.update_traces(marker=dict(
        color=color["hex"]))
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)