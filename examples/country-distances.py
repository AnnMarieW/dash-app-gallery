from dash import Dash, dcc, html, Input, Output, no_update
import plotly.express as px
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df = px.data.gapminder().query("year == 2007")

dropdown_country_a = dcc.Dropdown(
    id="country-distances-x-dropdown-a",
    options=df.country,
    value="Turkey",
)

dropdown_country_b = dcc.Dropdown(id="country-distances-x-dropdown-b")

info_card = dbc.Card(dbc.CardBody(html.P("Choose two countries and drag to rotate.")))

app.layout = dbc.Container(
    [
        html.H2("Country distances on map"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col([dropdown_country_a, dropdown_country_b], lg=6, sm=12),
                dbc.Col(info_card, lg=6, sm=12),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(id="country-distances-x-locations-graph"), lg=6, sm=12
                ),
                dbc.Col(dcc.Graph(id="country-distances-x-graph"), lg=6, sm=12),
            ]
        ),
    ]
)

# Callback for dropdown-b
@app.callback(
    Output("country-distances-x-dropdown-b", "options"),
    Output("country-distances-x-dropdown-b", "value"),
    Input("country-distances-x-dropdown-a", "value"),
    Input("country-distances-x-dropdown-b", "options"),
)
def set_dropdown_b_options(dropdown_a_value, dropdown_b_options):
    return (
        df[df.country != dropdown_a_value].country,
        "Canada" if dropdown_b_options is None else no_update,
    )


# Callback for line_geo graph
@app.callback(
    Output("country-distances-x-graph", "figure"),
    Output("country-distances-x-locations-graph", "figure"),
    Input("country-distances-x-dropdown-a", "value"),
    Input("country-distances-x-dropdown-b", "value"),
)
def make_line_geo_graph(country_a, country_b):
    dff = df[df.country.isin([country_a, country_b])]

    fig = px.line_geo(
        dff,
        locations="iso_alpha",
        projection="orthographic",
    )

    fig_locations = px.line_geo(
        dff, locations="iso_alpha", projection="orthographic", fitbounds="locations"
    )

    fig.update_traces(
        line_width=3,
        line_color="red",
    )

    fig_locations.update_traces(
        line_width=3,
        line_color="red",
    )

    return fig, fig_locations


if __name__ == "__main__":
    app.run_server(debug=True)
