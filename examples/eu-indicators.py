import pandas as pd
import requests
from dash import Dash, dcc, html, Input, Output, clientside_callback
import dash_bootstrap_components as dbc
import plotly.express as px
from io import StringIO

# This a link to the web interface where the data can be downloaded.
web_url = "https://sotkanet.fi/sotkanet/en/taulukko/?indicator=LclBCoAwEAPAF6WwWymFnMVnBBXrST0oCL7eFbyESUI_D00XsRCbyj0QVmX0hEJU5mTKhMdklVjjVrPIrJ0Yv-odkeVBoqmffxFP4AU=&region=s05zsy7TM4w3sjYCkvnWqXqGAA==&year=sy5ztk7V0zUEAA==&gender=m;f;t&abs=f&color=f&buildVersion=3.1.1&buildTimestamp=202211091024"

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Examle-Index/eu-indicators.csv')


indicators = sorted(list(df.Indicator.unique()))
countries = sorted(list(df.Country.unique()))

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Select an indicator"),
                        dcc.Dropdown(
                            id="eu-indicators-x-indicator-dropdown",
                            options=indicators,
                            value=indicators[0],
                            className="text-nowrap",
                        ),
                    ],
                    md=8,
                ),
                dbc.Col(
                    [
                        html.H2("Select a country"),
                        dcc.Dropdown(
                            id="eu-indicators-x-country-dropdown",
                            options=countries,
                            value=countries[0],
                        ),
                        dcc.Markdown(id="eu-indicators-x-available-countries"),
                    ]
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(id="eu-indicators-x-graph"),
                        html.Div(
                            [
                                "Data by ",
                                html.A(
                                    "Finnish Institute for Health and Welfare",
                                    href=web_url,
                                    target="_blank",
                                ),
                            ],
                            className="text-center fs-3 text",
                        ),
                        dbc.Button(
                            "Print Page",
                            id="eu-indicators-x-printing",
                            className="mt-2",
                        ),
                    ]
                )
            ],
            className="text-center",
        ),
        html.Div(id="eu-indicators-x-printing-hidden-content"),
    ]
)
@dash.clientside_callback(

    """
    function(clicks) {
        if (clicks > 0) {
          window.print()
        }
        return ""
    }
    """,
    Output("eu-indicators-x-printing-hidden-content", "children"),
    Input("eu-indicators-x-printing", "n_clicks"),
)

@app.callback(
    Output("eu-indicators-x-graph", "children"),
    Input("eu-indicators-x-indicator-dropdown", "value"),
    Input("eu-indicators-x-country-dropdown", "value"),
)
def update_indicator_graph(indicator, country):

    dff = df[(df.Indicator == indicator) & (df.Country == country)].dropna(axis=0)

    # In some cases there is only data for one year, so this line prevents notations such as '2016 - 2016'.
    title_text = {
        False: f"{dff.Year.min()} - {dff.Year.max()}",
        True: str(dff.Year.min()),
    }[dff.Year.min() == dff.Year.max()]
    dff.Year = dff.Year.astype(
        str
    )  # This is done to prevent the charts showing values between years (e.g. 2013.5).
    # if data has only one year create a bar chart, otherwise a scatter plot
    if dff["Year"].nunique() == 1:
        fig = px.bar(
            dff, x="Year", y="Val", color="Gender", barmode="group", height=500
        )
    else:
        fig = px.line(dff, x="Year", y="Val", color="Gender", height=500)
        fig.update_traces(mode="lines+markers", line=dict(width=3))
    fig.update_layout(
        title=dict(text=f"{indicator} in {country}<br>{title_text} by gender", x=0.5),
        yaxis=dict(title=indicator),
        xaxis=dict(title="Years"),
    )
    return dcc.Graph(figure=fig)

@app.callback(
    Output("eu-indicators-x-country-dropdown", "options"),
    Output("eu-indicators-x-country-dropdown", "value"),
    Output("eu-indicators-x-available-countries", "children"),
    Input("eu-indicators-x-indicator-dropdown", "value"),
)
def update_country_dropdown(indicator):

    dff = df[df.Indicator == indicator].dropna(axis=0)
    country_list = sorted(list(dff.Country.unique()))
    return (
        country_list,
        country_list[0],
        f"#### Available countries: {len(country_list)} / {len(countries)}",
    )
if __name__ == "__main__":
    app.run_server(debug=False)