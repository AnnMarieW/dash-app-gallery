from dash import Dash, dcc, html, Input, Output
import pandas as pd
from datetime import date
import plotly.express as px

filepath = "https://raw.githubusercontent.com/plotly/datasets/master/stockdata.csv"
df = pd.read_csv(filepath)
df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index(df["Date"]).drop(columns="Date")
new_df = df.diff(1)[1:]
df = df[1:]

stock_list = list(df.columns.values)

app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1(f'Stock Prices Time Series ({min(df.index.year)} to {max(df.index.year)})',
                style={'textAlign': 'center'})]),
    html.Div([
        html.H2('Enter a stock symbol, then select a date range:',
                style={"margin-left": "5em"}),
        html.Div(
            [
                dcc.Dropdown(
                    id='differenced-time-series-app-x-dropdown',
                    value='IBM',
                    options=stock_list,
                    multi=True,
                    style={'font-size': 20,
                           "margin-left": "3em"}
                )
            ], style={"width": "20%",
                      "display": "inline-block",
                      "verticalAlign": "middle"}
        ),
        html.Div(
            [dcc.DatePickerRange(
                id='differenced-time-series-app-x-date-picker',
                min_date_allowed=date(2007, 1, 4),
                max_date_allowed=date(2016, 3, 1),
                initial_visible_month=date(2016, 3, 1),
                start_date=date(2007, 1, 4),
                end_date=date(2016, 3, 1)
            )
            ],
            style={"width": "49%",
                   'font-size': 20,
                   "margin-left": "4em",
                   "display": "inline-block"}
        ),
        html.Div(
            [dcc.RadioItems(
                id="differenced-time-series-app-x-radio-items",
                options=["Stock Prices", "Returns"],
                value="Stock Prices"
            )
            ], style={"width": "50%",
                      'font-size': 20,
                      "margin-left": "-21em",
                      "display": "inline-block"}
        )
    ], style={"display": "inline-block", "width": "100%"}
    ),
    dcc.Graph(id='time-series-app-x-graph',
              style={"margin-left": "2.5em"})
]
)


@ app.callback(
    Output('differenced-time-series-app-x-graph', 'figure'),
    [Input("differenced-time-series-app-x-dropdown", "value"),
     Input("differenced-time-series-app-x-date-picker", "start_date"),
     Input("differenced-time-series-app-x-date-picker", "end_date"),
     Input("differenced-time-series-app-x-radio-items", "value")])
def update_graph(stock, start_date, end_date, graph_type):
    if graph_type == "Stock Prices":
        fig = px.line(df[start_date:end_date],
                      x=df[start_date:end_date].index,  y=stock)
        fig.update_layout()
        return fig
    elif graph_type == "Returns":
        fig = px.line(new_df[start_date:end_date],
                      x=df[start_date:end_date].index,  y=stock)
        fig.update_layout()
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)
