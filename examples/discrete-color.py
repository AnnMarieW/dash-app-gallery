from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = px.data.tips()

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Interactive color mode option with Dash"),
        html.P("Color mode:"),
        dcc.RadioItems(
            id="discrete-color-x-color-mode",
            value="discrete",
            options=["discrete", "continuous"],
        ),
        dcc.Graph(id="discrete-color-x-graph"),
    ]
)


@app.callback(
    Output("discrete-color-x-graph", "figure"),
    Input("discrete-color-x-color-mode", "value"),
)
def generate_chart(mode):
    if mode == "discrete":
        df["size"] = df["size"].astype(str)
    else:
        df["size"] = df["size"].astype(float)

    fig = px.scatter(
        df,
        x="total_bill",
        y="tip",
        color="size",
        title=f"'size' values mean using {mode.upper()} colors",
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
