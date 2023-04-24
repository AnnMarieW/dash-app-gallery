from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import dash_daq as daq
import plotly.io as pio
import time

df = px.data.gapminder()
df = df.loc[df["year"] == 1952]

# Set the template to ggplot2
# Here are all the default templates:
# "ggplot2", "seaborn", "simple_white", "plotly", "plotly_white", "plotly_dark", "presentation", "xgridoff", "ygridoff", "gridon", "none"
pio.templates.default = "ggplot2"

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H2("Interactive Bar Colour Control"),
        dcc.Loading(dcc.Graph(id="colourpicker-histogram-x-graph"), type="circle"),
        daq.ColorPicker(
            id="colourpicker-histogram-x-color",
            label="Color of Bars",
            size=164,
            value=dict(hex="#564AE6"),
        ),
    ]
)


@app.callback(
    Output("colourpicker-histogram-x-graph", "figure"),
    Input("colourpicker-histogram-x-color", "value"),
)
def update_points_color(color):
    fig = px.histogram(
        df,
        x="lifeExp",
        labels={"lifeExp": "Life Expectancy (years)"},
        title="Life Expectancy for Countries in 1952",
        nbins=23,
    )
    fig.update_layout(yaxis_title="Number of Countries")
    fig.update_traces(marker=dict(color=color["hex"]))
    time.sleep(
        2
    )  # simulate longer callback to make loading component (spinner) more visible
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
