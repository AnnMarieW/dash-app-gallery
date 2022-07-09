from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = px.data.tips()

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Interactive Plotly Express axes"),
        html.Button("Rotate labels", n_clicks=0, id="axes-x-button"),
        dcc.Graph(id="axes-x-graph"),
    ]
)


@app.callback(Output("axes-x-graph", "figure"), Input("axes-x-button", "n_clicks"))
def rotate_figure(n_clicks):
    fig = px.histogram(df, x="sex", height=500)
    fig.update_xaxes(tickangle=n_clicks * 45)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
