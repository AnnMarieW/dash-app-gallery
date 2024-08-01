import dash
from dash import Input, Output, dcc, html, ctx
import plotly.express as px
import dash_bootstrap_components as dbc

data_canada = px.data.gapminder().query("country == 'Canada'")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

buttons = html.Div(
    [
        dbc.Button("Bar chart", id="figures-with-ctx-x-btn-bar", color="secondary"),
        dbc.Button("Line chart", id="figures-with-ctx-x-btn-line", color="secondary"),
        dbc.Button(
            "Filled area chart", id="figures-with-ctx-x-btn-area", color="secondary"
        ),
    ],
    className="d-grid gap-2",
)

app.layout = dbc.Container(
    [
        html.H1("Changing figures with callback_context (CTX)"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col([buttons], md=4),
                dbc.Col(dcc.Graph(id="figures-with-ctx-x-graph"), md=8),
            ],
            align="center",
        ),
    ]
)


@app.callback(
    Output("figures-with-ctx-x-graph", "figure"),
    Input("figures-with-ctx-x-btn-bar", "n_clicks"),
    Input("figures-with-ctx-x-btn-line", "n_clicks"),
    Input("figures-with-ctx-x-btn-area", "n_clicks"),
)
def display(btn_bar, btn_line, btn_area):
    button_id = ctx.triggered_id

    if button_id == "figures-with-ctx-x-btn-bar":
        return px.bar(data_canada, x="year", y="pop")
    elif button_id == "figures-with-ctx-x-btn-line":
        return px.line(data_canada, x="year", y="pop")
    else:
        return px.area(data_canada, x="year", y="pop")


if __name__ == "__main__":
    app.run_server(debug=True)
