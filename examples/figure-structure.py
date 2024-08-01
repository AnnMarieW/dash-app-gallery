from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import json

fig = px.line(
    x=["a", "b", "c"],
    y=[1, 3, 2],
    title="sample figure",
    height=325,
)

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Displaying figure structure as JSON"),
        dcc.Graph(id="figure-structure-x-graph", figure=fig),
        dcc.Clipboard(target_id="figure-structure-x-structure"),
        html.Pre(
            id="figure-structure-x-structure",
            style={
                "border": "thin lightgrey solid",
                "overflowY": "scroll",
                "height": "275px",
            },
        ),
    ]
)


@app.callback(
    Output("figure-structure-x-structure", "children"),
    Input("figure-structure-x-graph", "figure"),
)
def display_structure(fig_json):
    return json.dumps(fig_json, indent=2)


if __name__ == "__main__":
    app.run_server(debug=True)
