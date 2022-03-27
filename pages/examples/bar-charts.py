from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)


app.layout = html.Div(
    [
        html.H4("Restaurant tips by day of week"),
        dcc.Dropdown(
            id="bar-chart-x-dropdown",
            options=["Fri", "Sat", "Sun"],
            value="Fri",
            clearable=False,
        ),
        dcc.Graph(id="bar-chart-x-graph"),
    ]
)


@app.callback(
    Output("bar-chart-x-graph", "figure"), Input("bar-chart-x-dropdown", "value")
)
def update_bar_chart(day):
    df = px.data.tips()  # replace with your own data source
    mask = df["day"] == day
    fig = px.bar(df[mask], x="sex", y="total_bill", color="smoker", barmode="group")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
