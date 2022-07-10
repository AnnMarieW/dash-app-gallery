from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = px.data.tips()

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Analysis of the restaurant sales"),
        dcc.Graph(id="pie-charts-x-graph"),
        html.P("Names:"),
        dcc.Dropdown(
            id="pie-charts-x-names",
            options=["smoker", "day", "time", "sex"],
            value="day",
            clearable=False,
        ),
        html.P("Values:"),
        dcc.Dropdown(
            id="pie-charts-x-values",
            options=["total_bill", "tip", "size"],
            value="total_bill",
            clearable=False,
        ),
    ]
)


@app.callback(
    Output("pie-charts-x-graph", "figure"),
    Input("pie-charts-x-names", "value"),
    Input("pie-charts-x-values", "value"),
)
def generate_chart(names, values):
    fig = px.pie(df, values=values, names=names, hole=0.3)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
