from dash import Dash, dcc, html, Input, Output, no_update
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# Defining the Dash application
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Countries data
df = px.data.gapminder().query("year == 2007")

# Country dropdown a
dropdown_country_a = dcc.Dropdown(
    id="country-distances-dropdown-a",
    options=[cntry for cntry in df.country],
    value="Turkey",
)

# Country dropdown b
dropdown_country_b = dcc.Dropdown(id="country-distances-dropdown-b")

# Application layout
app.layout = dbc.Container(
    [
        html.H2("Country distances on map"),
        html.Hr(),
        dbc.Row(dbc.Col([dropdown_country_a, dropdown_country_b], lg=12, sm=12)),
        dbc.Row(dbc.Col(dcc.Graph(id="country-distances-graph"), lg=12, sm=12)),
    ]
)

# Callback for dropdown-b
@app.callback(
    [
        Output("country-distances-dropdown-b", "options"),
        Output("country-distances-dropdown-b", "value"),
    ],
    [
        Input("country-distances-dropdown-a", "value"),
        Input("country-distances-dropdown-b", "options"),
    ],
)
def set_dropdown_b_options(dropdown_a_value, dropdown_b_options):
    return (
        [cntry for cntry in df[df.country != dropdown_a_value].country],
        "Canada" if dropdown_b_options is None else no_update,
    )


# Callback for line_geo graph
@app.callback(
    Output("country-distances-graph", "figure"),
    [
        Input("country-distances-dropdown-a", "value"),
        Input("country-distances-dropdown-b", "value"),
    ],
)
def make_line_geo_graph(country_a, country_b):

    dff = df[df.country.isin([country_a, country_b])]

    fig = px.line_geo(dff, locations="iso_alpha", projection="orthographic",)

    fig.update_traces(
        line_width=3, line_color="red",
    )

    return fig


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
