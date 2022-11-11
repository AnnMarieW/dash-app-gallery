# -*- coding: utf-8 -*-
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import orjson

# Data provided by Statistics Finland.
# Original data source: https://pxdata.stat.fi/PxWeb/pxweb/en/Kuntien_avainluvut/Kuntien_avainluvut__2021/kuntien_avainluvut_2021_viimeisin.px/
regions_data = pd.read_csv('assets/key_figures_regions.csv', encoding = 'latin-1').rename(columns ={'Region 2021':'Region'}).set_index('Region')

# Whole country figures on a pandas Dataframe.
# Extract information from the key figure names.
whole_country_df = pd.DataFrame(regions_data.loc['WHOLE COUNTRY'])
whole_country_df = whole_country_df.rename(columns = {'WHOLE COUNTRY':'value'})
whole_country_df['year'] = [stat.split(', ')[-1] for stat in whole_country_df.index]
whole_country_df['unit'] = [stat.split(', ')[-2] if len(stat.split(', ')) > 2 else '' for stat in whole_country_df.index]
whole_country_df['stat_name'] = [stat.split(', ')[0] if len(stat.split(', ')) < 4 else ', '.join(stat.split(', ')[:2]) for stat in whole_country_df.index]

# Drop since not needed.
regions_data.drop('WHOLE COUNTRY', axis = 0, inplace = True)

# The json file for the mapbox viz.
# https://geo.stat.fi/geoserver/wfs?service=WFS&version=2.0.0&request=GetFeature&typeName=maakunta1000k_2021&outputFormat=json
with open('assets/regions.json', encoding = 'ISO-8859-1') as f:
    regions_json = orjson.loads(f.read())

key_figures = sorted(list(pd.unique(regions_data.columns)))

external_stylesheets = [dbc.themes.SUPERHERO]

app = Dash(name = __name__, external_stylesheets = external_stylesheets)
app.title = "Finland's Regional Key Figures"
server = app.server


app.layout = dbc.Container([
        
        html.Div("Finland's Regional Key Figures",style={'textAlign':'center'}, className="mb-3 mt-3 fw-bold display-1"),

        dbc.Row([
            
            dbc.Col([
                html.H2('Key figure'),
                dcc.Dropdown(id = 'key-figures-finland-key-figure-selection-x',
                             options = [{'label':kf, 'value':kf} for kf in key_figures],
                             value = "Degree of urbanisation, %, 2020",
                             multi = False,
                             style = {'font-size':'1.2rem', 'font-family':'Arial','color': 'black', 'white-space': 'nowrap'}
                             ),
                html.Br(),
                html.H1(id = 'key-figures-finland-whole-country-header-x', style = {'textAlign':'center'}, className="mt-5 display-2"),
                html.Div(['Data by ',html.A('Statistics Finland', href = 'https://pxdata.stat.fi/PxWeb/pxweb/en/Kuntien_avainluvut/Kuntien_avainluvut__2021/kuntien_avainluvut_2021_viimeisin.px/', target = '_blank')], className="text-center fs-3 text"),
                
                ], xs = 12, sm = 12, md = 12, lg = 6, xl = 6, xxl = 6, align = 'center'),
                
            dbc.Col([
                html.H1(id = 'key-figures-finland-header-x', style = {'textAlign':'center'}, className="mb-3 mt-3 display-3"),
                dcc.Graph(id = 'key-figures-finland-region-map-x', figure = px.choropleth_mapbox(center = {"lat": 64.961093, "lon": 27.590605}))
                
                ], xs = 12, sm = 12, md = 12, lg = 6, xl = 6, xxl = 6)

            ], justify = 'center', className = "m-auto d-flex justify-content-center"),
  
        dcc.Store(id = 'key-figures-finland-locations-x'),
        dcc.Store(id = 'key-figures-finland-zs-x'),
        dcc.Store(id = 'key-figures-finland-geojson-data', data = regions_json),
        ], fluid = True)    

@app.callback(Output('key-figures-finland-header-x','children'),Input('key-figures-finland-key-figure-selection-x', 'value') )
def update_header(key_figure):
    return f"{key_figure} by region".capitalize()

@app.callback(Output('key-figures-finland-whole-country-header-x','children'),Input('key-figures-finland-key-figure-selection-x', 'value'))
def update_whole_country_header(key_figure):
    
    # Get all the header components.
    dff = whole_country_df.loc[key_figure]
    stat_name = dff.stat_name
    stat_unit = dff.unit
    stat_year = dff.year
    stat_value = dff.value
 
    # Change values with no decimals (.0) to int.
    stat_value = {True: int(stat_value), False: stat_value}['.0' in str(stat_value)]
    # Use space as thousand separator.
    stat_value = "{:,}".format(stat_value).replace(',',' ')
    
    return html.Div(
        [
            html.Div([stat_name, ", ", stat_year]),
            html.Div("in Finland"),
            html.Span([stat_value, " ", stat_unit]),
        ]
    )

@app.callback(

    Output('key-figures-finland-locations-x','data'),
    Output('key-figures-finland-zs-x','data'),
    Input('key-figures-finland-key-figure-selection-x','value')   
    
)
def store_data(key_figure):
    df = regions_data[key_figure]
    return list(df.index), list(df.values)

# Update map on clientside.
app.clientside_callback(

"""
    function(geojson, locations, z){           
       
        var layout = {
            'height':800,
            'mapbox': {'style':'open-street-map','zoom':4.2,'center':{'lat': 64.961093, 'lon': 27.590605}
            },
            'margin':{'l':0,'t':0,'b':0,'r':0
            }
        };
        var data = [{            
            'type':'choroplethmapbox',            
            'name':'',
            'subplot': 'mapbox',
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
Output('key-figures-finland-region-map-x', 'figure'),
Input('key-figures-finland-geojson-data','data'),
Input('key-figures-finland-locations-x','data'),
Input('key-figures-finland-zs-x','data')    
)

if __name__ == "__main__":
    app.run_server(debug=False)    