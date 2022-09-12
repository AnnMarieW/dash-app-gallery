# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 12:11:20 2022

@author: tuomas.poukkula

This code can be used alter the Dash bootstrap templates team 
and the graph themes back and forth.

"""

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url

dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css"
)
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])


iris = px.data.iris()
gapminder = px.data.gapminder()
tips = px.data.tips()
carshare = px.data.carshare()


graph_div = html.Div(id ='graphs', className="m-4")


graph_theme_switch = dcc.RadioItems(id = 'input-radio-button',
                                      options = [dict(label = 'Background Theme', value = 'Background Theme'),
                                                 dict(label = 'seaborn', value = 'seaborn'),
                                                 dict(label = 'ggplot2', value = 'ggplot2'),
                                                 dict(label = 'simple_white', value = 'simple_white'),
                                                 dict(label = 'plotly_white', value = 'plotly_white'),
                                                 dict(label = 'plotly_dark', value = 'plotly_dark'),
                                                 dict(label = 'presentation', value = 'presentation'),
                                                 dict(label = 'xgridoff', value = 'xgridoff'),
                                                 dict(label = 'ygridoff', value = 'ygridoff'),
                                                 dict(label = 'gridon', value = 'gridon'),
                                                 dict(label = 'none', value = 'none'),
                                                 ],
                                      inline=True,
                                      labelStyle = {'font-size':'1.2rem'},
                                      className = "d-flex justify-content-around",
                                      value = 'Background Theme')

app.layout = dbc.Container(
    [
        
        dbc.Row(
            [
                dbc.Col(
                    ThemeChangerAIO(
                        aio_id="theme", 
                        radio_props={"value": dbc.themes.SUPERHERO},
                        button_props={'size':'lg',
                                      'outline':False,
                                      'style':{'font-weight': 'bold'},
                                      'color':'success'}
                    ),
                    width=2,
                ),
                dbc.Col([graph_theme_switch], xs =12, sm=12, md=12, lg=6, xl=6,xxl=6),
            ],
            justify = 'center'
        ),
        graph_div,
        dbc.Row([
            
            dbc.Col([
                html.P('By Tuomas Poukkula'),
                html.Label(['Sources: ',
                    html.A("Dash Bootstrap Templates| ",
                            href = 'https://pypi.org/project/dash-bootstrap-templates/0.1.1/',
                            target = '_blank'
                            ),
                    html.A("Plotly Templates| ",
                            href = 'https://plotly.com/python/templates/',
                            target = '_blank'
                            ),
                    html.A("Plotly Express",
                            href = 'https://plotly.com/python/plotly-express/',
                            target = '_blank'
                            )
                    ])
                ])
            
            ])
    ],
    className="m-4 dbc",
    fluid=True,
)
@app.callback(
    Output("graphs", "children"), 
    [Input(ThemeChangerAIO.ids.radio("theme"), "value"),
      Input('input-radio-button','value')
      ]
)
def update_graph_theme(theme, plotly_template):
    
    if plotly_template == 'Background Theme':
        
        return [
        dbc.Row([
            dbc.Col([
                dcc.Graph(figure = px.scatter(iris, x="sepal_width", 
                                              y="sepal_length", 
                                              color="species", 
                                              height = 600,
                                              title = 'Iris',
                                              template = template_from_url(theme)
                                              )
                          )
                ],
                xs =12, sm=12, md=12, lg=6, xl=6,xxl=6
                ),
            dbc.Col([
                
                dcc.Graph(figure = px.scatter(gapminder, 
                                     x="gdpPercap", 
                                     y="lifeExp", 
                                     size="pop", 
                                     color="continent",
                                     hover_name="country", 
                                     animation_frame="year", 
                                     animation_group="country",  
                                     height = 600,
                                     log_x=True, 
                                     size_max=60,
                                     title = 'Gapminder',
                                     template = template_from_url(theme))
                          )
                
                ],xs =12, sm=12, md=12, lg=6, xl=6,xxl=6
                )
            ]),
        dbc.Row([
            
            dbc.Col([
                
                dcc.Graph(figure = px.violin(tips,
                                             y="tip", 
                                             x="smoker", 
                                             color="sex", 
                                             box=True, 
                                             points="all", 
                                             height = 600,
                                             hover_data=tips.columns,
                                             title = 'Tips',
                                             template = template_from_url(theme)
                                             )
                          )
                
                
                ],xs =12, sm=12, md=12, lg=6, xl=6,xxl=6
                ),
            dbc.Col([
                
                dcc.Graph(figure =px.scatter_mapbox(carshare, 
                                                    lat="centroid_lat", 
                                                    lon="centroid_lon", 
                                                    color="peak_hour", 
                                                    size="car_hours",
                                                    size_max=15, 
                                                    zoom=10,
                                                    height = 600,
                                                    mapbox_style="carto-positron",
                                                    title = 'Carshare',
                                                    template = template_from_url(theme))
                          )
                
                
                
                ],xs =12, sm=12, md=12, lg=6, xl=6,xxl=6
                )
            ])
        ]
    
    else:
        return [
        dbc.Row([
            dbc.Col([
                dcc.Graph(figure = px.scatter(iris, x="sepal_width", 
                                              y="sepal_length", 
                                              color="species", 
                                              height = 600,
                                              title = 'Iris',
                                              template = plotly_template
                                              )
                          )
                ],
                xs =12, sm=12, md=12, lg=6, xl=6,xxl=6
                ),
            dbc.Col([
                
                dcc.Graph(figure = px.scatter(gapminder, 
                                     x="gdpPercap", 
                                     y="lifeExp", 
                                     size="pop", 
                                     color="continent",
                                     hover_name="country", 
                                     animation_frame="year", 
                                     animation_group="country",                                     
                                     log_x=True, 
                                     size_max=60,
                                     height = 600,
                                     title = 'Gapminder',
                                     template = plotly_template)
                          )
                
                ],xs =12, sm=12, md=12, lg=6, xl=6,xxl=6
                )
            ]),
        dbc.Row([
            
            dbc.Col([
                
                dcc.Graph(figure = px.violin(tips,
                                             y="tip", 
                                             x="smoker", 
                                             color="sex", 
                                             box=True, 
                                             points="all", 
                                             height = 600,
                                             hover_data=tips.columns,
                                             title = 'Tips',
                                             template = plotly_template
                                             )
                          )
                
                
                ],xs =12, sm=12, md=12, lg=6, xl=6,xxl=6
                ),
            dbc.Col([
                
                dcc.Graph(figure =px.scatter_mapbox(carshare, 
                                                    lat="centroid_lat", 
                                                    lon="centroid_lon", 
                                                    color="peak_hour", 
                                                    size="car_hours",
                                                    size_max=15, 
                                                    zoom=10,
                                                    height = 600,
                                                    mapbox_style="carto-positron",
                                                    title = 'Carshare',
                                                    template = plotly_template)
                          )
                
                
                
                ],xs =12, sm=12, md=12, lg=6, xl=6,xxl=6
                )
            ])
        ]

if __name__ == "__main__":
    app.run_server(debug=True)