# !!!! impoprtant !!!!
# be sure to add:
# nameofthefile-x- 
# in front of every id, otherwise Dash will not work. Read more in readme.md

from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)


app.layout = html.Div([
    dcc.Graph(id="template-x-graph"),
    html.P("Title"),
    dcc.Input(id="template-x-title", value="", type="text"),
])


@app.callback(
    Output("template-x-graph", "figure"), 
    Input("template-x-component", "value"))
def display_(value):
    return 


if __name__ == "__main__":
    app.run_server(debug=True)
