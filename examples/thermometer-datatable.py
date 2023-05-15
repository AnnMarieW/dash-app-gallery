from dash import Dash, html, dcc, Input, Output
import dash_daq as daq
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import dash_ag_grid as dag

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/2016-weather-data-seattle.csv"
)
df["Date"] = pd.to_datetime(df["Date"])
df = df[df["Date"].dt.strftime("%Y") == "2015"]

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        html.H2("Filter a Data Table with Thermometer & Slider"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    daq.Thermometer(
                        id="thermometer-datatable-x-thermometer",
                        value=5,
                        min=0,
                        max=10,
                        style={"margin-bottom": "5%"},
                    )
                ),
                dbc.Col(
                    daq.Slider(
                        id="thermometer-datatable-x-slider",
                        min=0,
                        max=10,
                        value=5,
                        vertical=True,
                        size=200,
                    ),
                ),
                dbc.Col(
                    dag.AgGrid(
                        id="thermometer-datatable-x-table",
                        columnDefs=[{"field": i} for i in df.columns],
                        columnSize="responsiveSizeToFit",
                        style={"height":300}
                    ),
                    md=9,
                ),
            ],
            align="center",
        ),
        dbc.Row(
            dcc.Graph(
                figure=px.line(
                    df,
                    x="Date",
                    y="Mean_TemperatureC",
                    title="Seattle Mean Temperature in 2015",
                    height=350,
                )
            )
        ),
    ]
)


@app.callback(
    Output("thermometer-datatable-x-thermometer", "value"),
    Input("thermometer-datatable-x-slider", "value"),
)
def update_thermometer(value):
    return value


@app.callback(
    Output("thermometer-datatable-x-table", "rowData"),
    Input("thermometer-datatable-x-slider", "value"),
)
def update_table(value):
    dff = df.loc[df["Mean_TemperatureC"] == value]
    return dff.to_dict("records")


if __name__ == "__main__":
    app.run_server(debug=True)
