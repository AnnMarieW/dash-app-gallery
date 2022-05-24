from dash import dcc, html, Input, Output

from dash import Dash, dcc, html, Input, Output, dash_table, State
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# Read dataset into pandas dataframe
df = px.data.stocks()

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        html.Br(),
        html.H2("Download data example", style={'text-align': 'center'}),
        html.Br(),
        dcc.Download(id="dash_download_component_app-x-download"),

        dash_table.DataTable(df.to_dict('records'),
                             [{"name": i, "id": i} for i in df.columns],
                             page_size=10
                             ),

        html.Br(),

        # ------------------------------------------------ #
        # Starting bootstrap layout
        dbc.Row([

            dbc.Col([

                dcc.Dropdown(options=[
                    {'label': 'Excel file', 'value': 'excel'},
                    {'label': 'CSV file', 'value': 'csv'},
                ],
                    id='dash_download_component_app-x-dropdown',
                    placeholder='Choose download file type. Default is CSV format!')
            ]),

            dbc.Col([

                html.Button("Download Data", id="dash_download_component_app-x-btn_csv"),

                ]),

        ])
        # Ending bootstrap layout
        # ------------------------------------------------ #

])


@app.callback(
    Output("dash_download_component_app-x-download", "data"),
    Input("dash_download_component_app-x-btn_csv", "n_clicks"),
    State(component_id='dash_download_component_app-x-dropdown', component_property='value'),
    prevent_initial_call=True,
)
def func(n_clicks_btn, download_type):
    print(download_type)

    if download_type == 'csv':
        return dcc.send_data_frame(df.to_csv, "mydf.csv")
    else:
        return dcc.send_data_frame(df.to_excel, "mydf.xlsx")


if __name__ == "__main__":
    app.run_server(debug=True)

