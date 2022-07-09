from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = px.data.tips()

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Analysis of the restaurant's revenue"),
        html.P("x-axis:"),
        dcc.Checklist(
            id="box-plots-x-x-axis",
            options=["smoker", "day", "time", "sex"],
            value=["time"],
            inline=True,
        ),
        html.P("y-axis:"),
        dcc.RadioItems(
            id="box-plots-x-y-axis",
            options=["total_bill", "tip", "size"],
            value="total_bill",
            inline=True,
        ),
        dcc.Graph(id="box-plots-x-graph"),
    ]
)


@app.callback(
    Output("box-plots-x-graph", "figure"),
    Input("box-plots-x-x-axis", "value"),
    Input("box-plots-x-y-axis", "value"),
)
def generate_chart(x, y):
    fig = px.box(df, x=x, y=y)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
