from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv"
)

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Simple stock plot with adjustable axis"),
        html.Button("Switch Axis", n_clicks=0, id="plot-data-from-csv-x-button"),
        dcc.Graph(id="plot-data-from-csv-x-graph"),
    ]
)


@app.callback(
    Output("plot-data-from-csv-x-graph", "figure"),
    Input("plot-data-from-csv-x-button", "n_clicks"),
)
def display_graph(n_clicks):
    if n_clicks % 2 == 0:
        x, y = "AAPL_x", "AAPL_y"
    else:
        x, y = "AAPL_y", "AAPL_x"

    fig = px.line(df, x=x, y=y)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
