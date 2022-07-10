from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = px.data.medals_wide(indexed=True)

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Olympic medals won by countries"),
        dcc.Graph(id="heatmaps-x-graph"),
        html.P("Medals included:"),
        dcc.Checklist(
            id="heatmaps-x-medals",
            options=["gold", "silver", "bronze"],
            value=["gold", "silver"],
        ),
    ]
)


@app.callback(Output("heatmaps-x-graph", "figure"), Input("heatmaps-x-medals", "value"))
def filter_heatmap(cols):
    fig = px.imshow(df[cols])
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
