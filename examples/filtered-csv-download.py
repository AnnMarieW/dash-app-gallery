import dash
import pandas as pd
from dash import Dash,  dcc, html, Input, Output, State
import dash_ag_grid as dag
import plotly.express as px

app = Dash()

df = px.data.gapminder()

range_slider = dcc.RangeSlider(
    value=[1987, 2007],
    step=5,
    marks={i: str(i) for i in range(1952, 2012, 5)},
)

dtable = dag.AgGrid(
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],
)

download_button = dcc.Button("Download Filtered CSV", style={"marginTop": 20})
download_component = dcc.Download()

app.layout = html.Div(
    [
        html.H2("Gapminder data filtered download", style={"marginBottom": 20}),
        download_component,
        range_slider,
        download_button,
        dtable,
    ]
)


@app.callback(
    Output(dtable, "dashGridOptions"),
    Input(range_slider, "value"),
)
def update_table(slider_value):
    if not slider_value:
        return dash.no_update

    return {
        "isExternalFilterPresent": {"function": "true"},
        "doesExternalFilterPass": {"function": f"params.data.year >= {slider_value[0]} && params.data.year <= {slider_value[1]}"}
    }


@app.callback(
    Output(download_component, "data"),
    Input(download_button, "n_clicks"),
    State(dtable, "virtualRowData"),
    prevent_initial_call=True,
)
def download_data(n_clicks, data):
    dff = pd.DataFrame(data)
    return dcc.send_data_frame(dff.to_csv, "filtered_csv.csv")


if __name__ == "__main__":
    app.run(debug=True)
