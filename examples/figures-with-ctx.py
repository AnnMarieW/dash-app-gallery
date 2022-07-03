import dash
from dash import Input, Output, dcc, html, ctx
import plotly.express as px
import dash_bootstrap_components as dbc

# Reading the data
data_canada = px.data.gapminder().query("country == 'Canada'")

# Defining the Dash application
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

buttons = html.Div(
    [
        html.Button("Bar chart", id="figures-with-ctx-x-btn-bar"),
        html.Br(),
        html.Button("Line chart", id="figures-with-ctx-x-btn-line"),
        html.Br(),
        html.Button("Filled area chart", id="figures-with-ctx-x-btn-area"),
    ]
)

# Application layout
app.layout = dbc.Container(
    [
        html.H1("Changing figures with callback_context (CTX)"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col([buttons], lg=4, sm=12),
                dbc.Col(dcc.Graph(id="figures-with-ctx-x-graph"), lg=8, sm=12),
            ],
            align="center",
        ),
    ]
)

# Callback
@app.callback(
    Output("figures-with-ctx-x-graph", "figure"),
    Input("figures-with-ctx-x-btn-bar", "n_clicks"),
    Input("figures-with-ctx-x-btn-line", "n_clicks"),
    Input("figures-with-ctx-x-btn-area", "n_clicks"),
)
def display(btn_bar, btn_line, btn_area):
    button_id = ctx.triggered_id if ctx.triggered_id else "figures-with-ctx-x-btn-bar"

    if button_id == "figures-with-ctx-x-btn-bar":
        return px.bar(data_canada, x="year", y="pop")
    elif button_id == "figures-with-ctx-x-btn-line":
        return px.line(data_canada, x="year", y="pop")
    else:
        return px.area(data_canada, x="year", y="pop")


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
