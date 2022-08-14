from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = px.data.stocks()

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Stock price analysis"),
        dcc.Graph(id="time-series-x-time-series-chart"),
        html.P("Select stock:"),
        dcc.Dropdown(
            id="time-series-x-ticker",
            options=["AMZN", "FB", "NFLX"],
            value="AMZN",
            clearable=False,
        ),
    ]
)


@app.callback(
    Output("time-series-x-time-series-chart", "figure"),
    Input("time-series-x-ticker", "value"),
)
def display_time_series(ticker):
    fig = px.line(df, x="date", y=ticker)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
