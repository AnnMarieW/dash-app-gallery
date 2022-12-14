import pandas as pd
import requests
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from io import StringIO

# This a link to the web interface where the data can be downloaded.
web_url = "https://sotkanet.fi/sotkanet/en/taulukko/?indicator=LclBCoAwEAPAF6WwWymFnMVnBBXrST0oCL7eFbyESUI_D00XsRCbyj0QVmX0hEJU5mTKhMdklVjjVrPIrJ0Yv-odkeVBoqmffxFP4AU=&region=s05zsy7TM4w3sjYCkvnWqXqGAA==&year=sy5ztk7V0zUEAA==&gender=m;f;t&abs=f&color=f&buildVersion=3.1.1&buildTimestamp=202211091024"

# This is the download link. In order to read it in pandas, one needs to convert it into StringIO first.
file_url = 'https://sotkanet.fi/sotkanet/en/csv?indicator=LclBCoAwEAPAF6WwWymFnMVnBBXrST0oCL7eFbyESUI_D00XsRCbyj0QVmX0hEJU5mTKhMdklVjjVrPIrJ0Yv-odkeVBoqmffxFP4AU=&region=s05zsy7TM4w3sjYCkvnWqXqGAA==&year=sy5ztk7V0zUEAA==&gender=m;f;t&abs=f&color=f&buildVersion=3.1.1&buildTimestamp=202211091024&order=G'

# The headers are there to mimic the user and to show the target server that the one who is trying to access the file is a person and not a bot.
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
 'Content-Type': 'text/html; charset=utf-8'}

bytes_data = requests.get(file_url,headers=headers).content
s = str(bytes_data,'utf-8')
data = StringIO(s) 
df = pd.read_csv(data,sep=';', header=None)   
df = df.set_index(list(df.columns[:-2])).dropna(axis=0, how='all').reset_index()
df.drop([1,3,7],axis=1, inplace = True)
df.columns = ['Indicator','Country', 'Gender','Year','Val']
df.Val = df.Val.str.replace(',','.').astype(float)

indicators = sorted(list(df.Indicator.unique()))
countries = sorted(list(df.Country.unique()))

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Select an indicator"),
                        dcc.Dropdown(
                            id="eu-indicators-indicator-dropdown-x",
                            options=indicators,
                            value=indicators[0],
                            className="text-nowrap",
                        ),
                    ],
                    md = 8,
                ),
                dbc.Col(
                    [
                        html.H2("Select a country"),
                        dcc.Dropdown(
                            id="eu-indicators-country-dropdown-x",
                            options=countries,
                            value=countries[0],
                        ),
                        dcc.Markdown(id="eu-indicators-available-countries-x"),
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(id="eu-indicators-graph-x"),
                        html.Div(
                            [ "Data by ",
                                html.A("Finnish Institute for Health and Welfare",href=web_url,target="_blank"),
                            ],
                            className="text-center fs-3 text",
                        ),
                        dbc.Button("Print Page", id="eu-indicators-printing-x", className = 'mt-2'),
                    ]
                )
            ],
            style={"textAlign": "center"},
        ),
        html.Div(id="eu-indicators-printing-hidden-content-x"),
    ]
)
app.clientside_callback(
    """
    function(clicks) {
        if (clicks > 0) {
          window.print()
        }
        return ""
    }
    """,
    Output("eu-indicators-printing-hidden-content-x", "children"),
    Input("eu-indicators-printing-x", "n_clicks"),
)

@app.callback(
    Output("eu-indicators-graph-x", "children"),
    Input("eu-indicators-indicator-dropdown-x", "value"),
    Input("eu-indicators-country-dropdown-x", "value")
)
def update_indicator_graph(indicator, country):

    dff = df[(df.Indicator == indicator) & (df.Country == country)].dropna(axis=0)

    # In some cases there is only data for one year, so this line prevents notations such as '2016 - 2016'.  
    title_text = {False: f"{dff.Year.min()} - {dff.Year.max()}", True: str(dff.Year.min())}[
        dff.Year.min() == dff.Year.max()
    ]

    traces = []
    for gender in dff.Gender.unique():

        dfff = dff[dff.Gender == gender]


        if len(dfff) > 1:
            traces.append(
                go.Scatter(x=dfff.Year.astype(str), y=dfff.Val, name=gender, showlegend=True)
            )
        else:
            traces.append(
                go.Bar(x=dfff.Year.astype(str), y=dfff.Val,name=gender,showlegend=True)
            )
          
    
    return dcc.Graph(
        figure=go.Figure(
            data=traces,
            layout=go.Layout(
                title=dict(
                    text=f"{indicator} in {country}<br>{title_text} by gender", x=0.5
                ),
                xaxis=dict(title="Years"),
                yaxis=dict(title=indicator),
                legend = dict(title = 'Gender'),
                height = 600
            ),
        )
    )
@app.callback(
    Output("eu-indicators-country-dropdown-x", "options"),
    Output("eu-indicators-country-dropdown-x", "value"),
    Output("eu-indicators-available-countries-x", "children"),
    Input("eu-indicators-indicator-dropdown-x", "value"),
)
def update_country_dropdown(indicator):

    dff = df[df.Indicator == indicator].dropna(axis=0)

    country_list = sorted(list(dff.Country.unique()))
    return country_list, country_list[0], f"#### Available countries: {len(country_list)} / {len(countries)}",
    
if __name__ == "__main__":
    app.run_server(debug=True)
