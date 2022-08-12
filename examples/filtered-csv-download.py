
import pandas as pd
from dash import Dash, dash_table, dcc, html, Input, Output, State
import plotly.express as px

app = Dash(__name__)

df = px.data.gapminder()

range_slider = dcc.RangeSlider(
    value=[1987, 2007],
    step=5,
    marks={i: str(i) for i in range(1952, 2012, 5)},
)

dtable = dash_table.DataTable(
    columns=[{"name": i, "id": i} for i in sorted(df.columns)],
    page_size=10,
)

download_button = html.Button("Download Filtered CSV")
download_component = dcc.Download()

app.layout = html.Div(
    [
        html.H2("Gapminder data filtered download"),
        download_component,
        range_slider,
        download_button,
        dtable,
    ]
)


@app.callback(
    Output(dtable, "data"),
    Input(range_slider, "value"),
)
def update_table(slider_value):
    return df[df.year.between(slider_value[0], slider_value[1])].to_dict("records")


@app.callback(
    Output(download_component, "data"),
    Input(download_button, "n_clicks"),
    State(dtable, "derived_virtual_data"),
    prevent_initial_call=True,
)
def download_data(n_clicks, data):
    dff = pd.DataFrame(data)
    return dcc.send_data_frame(dff.to_csv, "filtered_csv.csv")


if __name__ == "__main__":
    app.run_server(debug=True)