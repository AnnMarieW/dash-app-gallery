from dash import Dash, dcc, html, Input, Output, dash_table, State
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
                        dash_table.DataTable(
                            df.to_dict("records"),
                            [{"name": i, "id": i} for i in df.columns],
                            page_size=10,
                            style_table={"overflowX": "auto"},
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
    app.run_server(debug=True)
