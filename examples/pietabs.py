from dash import Dash, dcc, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_table(
    "https://raw.githubusercontent.com/plotly/datasets/master/global_super_store_orders.tsv"
)
df = df[df["Country"].isin(["China", "Germany", "United States", "France"])]
df["ship_date"] = pd.to_datetime(df["Ship Date"], format='%m/%d/%y')

# convert shipping costs and profit from strings to floats
df["Shipping Cost"] = df["Shipping Cost"].str.replace(",", ".").astype("float")


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dcc.Markdown(
            "#### Shipping costs breakdown by country and category",
            style={"textAlign": "center"},
            className="my-4",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.DatePickerRange(
                            id="pietabs-x-datepicker",
                            min_date_allowed=min(df["ship_date"]),
                            max_date_allowed=max(df["ship_date"]),
                            end_date=max(df["ship_date"]),
                            start_date=min(df["ship_date"]),
                            clearable=False,
                        ),
                    ],
                    width=4,
                ),
                dbc.Col(
                    [
                        dcc.Tabs(
                            id="pietabs-x-tabs",
                            value="pietabs-x-tab-1",
                            children=[
                                dcc.Tab(
                                    label="Country",
                                    value="pietabs-x-tab-1",
                                    children=[dcc.Graph(id="pietabs-x-pie1")],
                                ),
                                dcc.Tab(
                                    label="Category",
                                    value="pietabs-x-tab-2",
                                    children=[dcc.Graph(id="pietabs-x-pie2")],
                                ),
                            ],
                        ),
                    ],
                    width=8,
                ),
            ]
        ),
    ]
)


@app.callback(
    Output("pietabs-x-pie1", "figure"),
    Output("pietabs-x-pie2", "figure"),
    Input("pietabs-x-datepicker", "start_date"),
    Input("pietabs-x-datepicker", "end_date"),
)
def render_content(start_date, end_date):
    dff = df.query("ship_date > @start_date & ship_date < @end_date")

    pie1_fig = px.pie(dff, values="Shipping Cost", names="Country")

    pie2_fig = px.pie(dff, values="Shipping Cost", names="Category")

    return (pie1_fig, pie2_fig)


if __name__ == "__main__":
    app.run_server(debug=True)
