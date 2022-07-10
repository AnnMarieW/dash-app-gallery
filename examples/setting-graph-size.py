from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = px.data.tips()

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Live adjustable graph-size"),
        html.P("Change figure width:"),
        dcc.Slider(
            id="setting-graph-size-x-slider",
            min=200,
            max=500,
            step=25,
            value=300,
            marks={x: str(x) for x in [200, 300, 400, 500]},
        ),
        dcc.Graph(id="setting-graph-size-x-graph"),
    ]
)


@app.callback(
    Output("setting-graph-size-x-graph", "figure"),
    Input("setting-graph-size-x-slider", "value"),
)
def resize_figure(width):
    fig = px.scatter(df, x="total_bill", y="tip", facet_col="sex", height=400)
    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="LightSteelBlue",
    )
    fig.update_layout(width=int(width))

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
