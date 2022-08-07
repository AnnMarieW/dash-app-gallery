from dash import Dash, dash_table, dcc, html, Input, Output, ctx
import plotly.express as px
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df = px.data.gapminder()

marks = {}
for i in range(1952, 2012, 5):
    marks[i] = str(i)

dtable = dash_table.DataTable(
    id="filtered-csv-download-datatable",
    columns=[{"name": i, "id": i} for i in sorted(df.columns)],
    page_current=0,
    page_size=10,
    page_action="custom",
)

download_layout = html.Div(
    [
        dbc.Button("Download Filtered CSV", id="filtered-csv-download-btn"),
        dcc.Download(id="filtered-csv-download-dataframe"),
    ]
)

app.layout = dbc.Container(
    [
        html.H2("Gapminder data filtered download"),
        html.Hr(),
        dbc.Row(dbc.Col(download_layout)),
        dbc.Row(
            dbc.Col(
                dcc.RangeSlider(
                    value=[1987, 2007],
                    step=5,
                    marks=marks,
                    id="filtered-csv-download-slider",
                )
            ),
        ),
        dbc.Row(dbc.Col(dtable)),
    ]
)

# Callback for updating the slider
@app.callback(
    Output("filtered-csv-download-slider", "min"),
    Output("filtered-csv-download-slider", "max"),
    Output("filtered-csv-download-slider", "value"),
    Input("filtered-csv-download-slider", "value"),
)
def update_output(value):
    return df.year.min(), df.year.max(), value


# Callback for updating the datatable
@app.callback(
    Output("filtered-csv-download-datatable", "data"),
    Input("filtered-csv-download-slider", "value"),
    Input("filtered-csv-download-datatable", "page_current"),
    Input("filtered-csv-download-datatable", "page_size"),
)
def update_table(slider_value, page_current, page_size):
    dff = df[df.year.between(slider_value[0], slider_value[1])]

    return dff.iloc[page_current * page_size : (page_current + 1) * page_size].to_dict(
        "records"
    )


# Callback for downloading the filtered data
@app.callback(
    Output("filtered-csv-download-dataframe", "data"),
    Input("filtered-csv-download-slider", "value"),
    Input("filtered-csv-download-btn", "n_clicks"),
    prevent_initial_call=True,
)
def download_data(slider_value, n_clicks):
    dff = df[df.year.between(slider_value[0], slider_value[1])]

    if "filtered-csv-download-btn" == ctx.triggered_id:
        return dcc.send_data_frame(dff.to_csv, "filtered_csv.csv")


if __name__ == "__main__":
    app.run_server(debug=True)
