# -*- coding: utf-8 -*-
import pandas as pd
from dash import Dash, dcc, html, Input, Output, clientside_callback
import dash_bootstrap_components as dbc
import plotly.express as px
import requests

# Data provided by Statistics Finland.
# Original data source: https://pxdata.stat.fi/PxWeb/pxweb/en/Kuntien_avainluvut/Kuntien_avainluvut__2021/kuntien_avainluvut_2021_viimeisin.px/
df = (
    pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/Dash-Examle-Index/key_figures_regions.csv", encoding="utf-8")
    .rename(columns={"Region 2021": "Region"})
    .set_index("Region")
)

# Whole country figures on a pandas Dataframe.
# Extract information from the key figure names to be used in callbacks.
whole_country_df = pd.DataFrame(df.loc["WHOLE COUNTRY"])
whole_country_df = whole_country_df.rename(columns={"WHOLE COUNTRY": "value"})
whole_country_df["year"] = [stat.split(", ")[-1] for stat in whole_country_df.index]
whole_country_df["unit"] = [
    stat.split(", ")[-2] if len(stat.split(", ")) > 2 else ""
    for stat in whole_country_df.index
]
whole_country_df["stat_name"] = [
    stat.split(", ")[0]
    if len(stat.split(", ")) < 4
    else ", ".join(stat.split(", ")[:2])
    for stat in whole_country_df.index
]

# Drop since not needed.
df.drop("WHOLE COUNTRY", axis=0, inplace=True)

# The json file used for the mapbox viz.
# https://geo.stat.fi/geoserver/wfs?service=WFS&version=2.0.0&request=GetFeature&typeName=maakunta1000k_2021&outputFormat=json
r = requests.get(r"https://raw.githubusercontent.com/plotly/datasets/master/Dash-Examle-Index/regions.json")
r.encoding='utf-8'
regions_json = r.json()

external_stylesheets = [dbc.themes.SPACELAB]

app = Dash(name=__name__, external_stylesheets=external_stylesheets)

app.layout = dbc.Container(
    [
        html.Div(
            "Finland's Regional Key Figures",
            className="text-center mb-3 mt-3 fw-bold display-1",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Key figure"),
                        dcc.Dropdown(
                            id="key-figures-finland-x-key-figure-selection",
                            options=sorted(list(pd.unique(df.columns))),
                            value="Degree of urbanisation, %, 2020",
                            className="text-nowrap",
                        ),
                        html.H3(
                            id="key-figures-finland-x-whole-country-header",
                            className="mt-5 display-3 text-center",
                        ),
                        html.Div(
                            [
                                "Data by ",
                                html.A(
                                    "Statistics Finland",
                                    href="https://pxdata.stat.fi/PxWeb/pxweb/en/Kuntien_avainluvut/Kuntien_avainluvut__2021/kuntien_avainluvut_2021_viimeisin.px/",
                                    target="_blank",
                                ),
                            ],
                            className="text-center fs-3 text",
                        ),
                    ],
                    md=6,
                    align="center",
                ),
                dbc.Col(
                    [
                        dcc.Graph(
                            id="key-figures-finland-x-region-map",
                            figure=px.choropleth_mapbox(
                                center={"lat": 64.961093, "lon": 25.795386}
                            ),
                        )
                    ],
                    md=6,
                ),
            ],
            justify="center",
        ),
        dcc.Store(id="key-figures-finland-x-locations"),
        dcc.Store(id="key-figures-finland-x-zs"),
        dcc.Store(id="key-figures-finland-x-geojson-data", data=regions_json),
    ],
    fluid=True,
)


@app.callback(
    Output("key-figures-finland-x-whole-country-header", "children"),
    Input("key-figures-finland-x-key-figure-selection", "value"),
)
def update_whole_country_header(key_figure):
    dff = whole_country_df.loc[key_figure]

    # Change values with no decimals (.0) to int.
    stat_value = {True: int(dff.value), False: dff.value}[".0" in str(dff.value)]

    return html.Div(
        [
            html.Div([dff.stat_name, ", ", dff.year]),
            html.Div("in Finland"),
            html.Span([f"{stat_value:,}", " ", dff.unit]),
        ],
    )


@app.callback(
    Output("key-figures-finland-x-locations", "data"),
    Output("key-figures-finland-x-zs", "data"),
    Input("key-figures-finland-x-key-figure-selection", "value"),
)
def store_data(key_figure):
    dff = df[key_figure]
    return list(dff.index), list(dff.values)


# Update map on clientside for better performance
clientside_callback(
    """
    function(geojson, locations, z){           
       
        var layout = {
            'height':600,
            'mapbox': {'style':'open-street-map','zoom':3.8,'center':{'lat': 64.961093, 'lon': 25.795386}
            },
            'margin':{'l':0,'t':0,'b':0,'r':0}
        };
        var data = [{            
            'type':'choroplethmapbox',            
            'name':'',
            'geojson':geojson,
            'locations':locations,
            'featureidkey':'properties.name',
            'hovertemplate': '<b>%{location}</b><br>%{z:,}',
            'hoverlabel':{'font':{'family':'Arial Black', 'size':20, 'color':'black'},'bgcolor':'white'},
            'z':z,
            'colorscale':'Viridis'
        }];
        return {'data':data,'layout':layout}
    }   
""",
    Output("key-figures-finland-x-region-map", "figure"),
    Input("key-figures-finland-x-geojson-data", "data"),
    Input("key-figures-finland-x-locations", "data"),
    Input("key-figures-finland-x-zs", "data"),
)

if __name__ == "__main__":
    app.run_server(debug=False)
