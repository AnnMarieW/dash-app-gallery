from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import json, urllib

url = "https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Supply chain of the energy production"),
        dcc.Graph(id="sankey-diagram-x-graph"),
        html.P("Opacity"),
        dcc.Slider(id="sankey-diagram-x-slider", min=0, max=1, value=0.5, step=0.1),
    ]
)


@app.callback(
    Output("sankey-diagram-x-graph", "figure"),
    Input("sankey-diagram-x-slider", "value"),
)
def display_sankey(opacity):
    node = data["data"][0]["node"]
    node["color"] = [
        f"rgba(255,0,255,{opacity})"
        if c == "magenta"
        else c.replace("0.8", str(opacity))
        for c in node["color"]
    ]

    link = data["data"][0]["link"]
    link["color"] = [node["color"][src] for src in link["source"]]

    fig = go.Figure(go.Sankey(link=link, node=node))
    fig.update_layout(font_size=10)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
