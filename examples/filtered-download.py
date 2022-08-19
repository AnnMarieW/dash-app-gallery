from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from base64 import b64encode
import io

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv"
)
df = df[["City", "State", "Population"]]

dropdown_state = dcc.Dropdown(
    id="filtered-download-x-dropdown", options=df.State, value="New York"
)

download_button = html.A(
    html.Button("Download as HTML"),
    id="filtered-download-x-href",
    href="filtered-download-x-href",
    download="plotly_graph.html",
)

app.layout = dbc.Container(
    [
        html.H2("U.S. Top 10 City Populations by State"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col([dropdown_state, download_button], md=6, sm=12),
                dbc.Col(dcc.Graph(id="filtered-download-x-graph")),
            ]
        ),
    ]
)


@app.callback(
    Output("filtered-download-x-graph", "figure"),
    Output("filtered-download-x-href", "href"),
    Input("filtered-download-x-dropdown", "value"),
)
def update_bar_chart(state):

    dff = df[df.State == state].sort_values(by="Population").head(10)

    fig = px.bar(dff, x="Population", y="City", text="Population")

    buffer = io.StringIO()
    fig.write_html(buffer)
    html_bytes = buffer.getvalue().encode()
    encoded = b64encode(html_bytes).decode()
    href = "data:text/html;base64," + encoded

    return fig, href


if __name__ == "__main__":
    app.run_server(debug=True)
