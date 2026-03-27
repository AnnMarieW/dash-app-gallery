from dash import Dash, dcc, html, Input, Output, State
import dash_ag_grid as dag
import plotly.express as px
import dash_bootstrap_components as dbc


df = px.data.stocks()

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [html.H2("Download data example", style={"text-align": "center"})]
                )
            ]
        ),
        dcc.Download(id="dash_download_component_app-x-download"),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dag.AgGrid(
                            rowData=df.to_dict("records"),
                            columnDefs=[{"field": i} for i in df.columns],
                        )
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Dropdown(
                            options=[
                                {"label": "Excel file", "value": "excel"},
                                {"label": "CSV file", "value": "csv"},
                            ],
                            id="dash_download_component_app-x-dropdown",
                            placeholder="Choose download file type. Default is CSV format!",
                        )
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Button(
                            "Download Data", id="dash_download_component_app-x-btn_csv"
                        ),
                    ]
                ),
            ]
        ),
    ]
)


@app.callback(
    Output("dash_download_component_app-x-download", "data"),
    Input("dash_download_component_app-x-btn_csv", "n_clicks"),
    State("dash_download_component_app-x-dropdown", "value"),
    prevent_initial_call=True,
)
def func(n_clicks_btn, download_type):
    if download_type == "csv":
        return dcc.send_data_frame(df.to_csv, "mydf.csv")
    else:
        return dcc.send_data_frame(df.to_excel, "mydf.xlsx")


if __name__ == "__main__":
    app.run(debug=True)
