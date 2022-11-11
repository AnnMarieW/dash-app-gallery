# -*- coding: utf-8 -*-
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import orjson

# Data provided by Statistics Finland.
regions_data = pd.read_csv('./assets/key_figures_regions.csv', encoding = 'latin-1').rename(columns ={'Region 2021':'Region'}).set_index('Region')

# Whole country figures on a pandas Series.
whole_country_df = regions_data.loc['WHOLE COUNTRY']

# Drop since not needed.
regions_data.drop('WHOLE COUNTRY', axis = 0, inplace = True)

# The json file for the mapbox viz.
# https://geo.stat.fi/geoserver/wfs?service=WFS&version=2.0.0&request=GetFeature&typeName=maakunta1000k_2021&outputFormat=json
with open('assets/regions.json', encoding = 'ISO-8859-1') as f:
    regions_json = orjson.loads(f.read())
    
    
def draw_map(figure):    
    
    fig = px.choropleth_mapbox(regions_data[[figure]].reset_index(), 
                               geojson=regions_json, 
                               locations='Region', 
                               color=figure,
                               mapbox_style="open-street-map",
                               featureidkey='properties.name',
                               zoom=4.2,
                               labels = {figure:figure},
                               color_continuous_scale='Viridis',
                               center = {"lat": 64.961093, "lon": 27.590605}
                          )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
                      height=800,
                      hoverlabel = {'font':{'family':'Arial Black', 'size':20, 'color':'black'},'bgcolor':'white'},
                      
                      )
    return fig
    

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
                             style = {'font-size':20, 'font-family':'Arial','color': 'black'}
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

        ], fluid = True)    

@app.callback(

    Output('key-figures-finland-region-map-x','figure'),
    Input('key-figures-finland-key-figure-selection-x','value')
)
def update_map_figure(key_figure):
    return draw_map(key_figure)

@app.callback(Output('key-figures-finland-header-x','children'),Input('key-figures-finland-key-figure-selection-x', 'value') )
def update_header(key_figure):
    return f"{key_figure} by region".capitalize()

@app.callback(Output('key-figures-finland-whole-country-header-x','children'),Input('key-figures-finland-key-figure-selection-x', 'value'))
def update_whole_country_header(key_figure):
    kf_string = key_figure.split(',')
    kf_string.pop(-2)
    kf_string = ', '.join(kf_string)
    kf_string = {True:key_figure, False:kf_string}[len(kf_string.split(','))==1]
    return html.P([kf_string,html.Br(),"in Finland:",html.Br(), ("{:,}".format(whole_country_df.loc[key_figure])).replace('.0','').replace(',',' ')+key_figure.split(',')[-2].replace('2020','').replace('2021','').replace(key_figure.split(',')[0],'')],className="fw-bold")

if __name__ == "__main__":
    app.run_server(debug=False)    