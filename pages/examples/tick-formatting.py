from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Live tick formatting"),
        dcc.Checklist(
            id="tick-formatting-x-tick",
            options=[{"label": "Enable linear ticks", "value": "linear"}],
            value=["linear"],
        ),
        dcc.Graph(id="tick-formatting-x-graph"),
    ]
)


@app.callback(
    Output("tick-formatting-x-graph", "figure"),
    Input("tick-formatting-x-tick", "value"),
)
def display_figure(tick_mode):
    fig = go.Figure(
        go.Scatter(  # replace with your own data source
            x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            y=[28.8, 28.5, 37, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9],
        )
    )
    if "linear" in tick_mode:
        fig.update_layout(xaxis=dict(tickmode="linear", tick0=0.5, dtick=0.75))
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
