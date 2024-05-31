import pandas as pd
from dash import Dash, Input, Output, callback, dcc, html, State
import plotly.express as px
import dash_bootstrap_components as dbc


df = pd.read_table(
    "https://raw.githubusercontent.com/plotly/datasets/master/global_super_store_orders.tsv"
)


df["profit_derived"] = df["Profit"].str.replace(",", ".").astype("float")
df["ship_date"] = pd.to_datetime(df["Ship Date"], format='%m/%d/%y')

# Hierarchical charts work only with positive aggregate values
# In this step, we ensure that aggregated values will be positive
df = df.query(expr="profit_derived >= 0")

df = df[["profit_derived", "Segment", "Region", "ship_date"]]


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = dbc.Container(
    [
        html.H4(
            "Where does profit come from? - Looking at profit through segment and region dimension.",
            style={"textAlign": "center"},
            className="mb-3 mt-3",
        ),
        html.Div(
            [
                dbc.Button(
                    "Open Filters", id="offCanvas_icicle-x-open-offcanvas", n_clicks=0
                ),
                dbc.Offcanvas(
                    [
                        html.Label("Region"),
                        dcc.Dropdown(
                            id="offCanvas_icicle-x-dynamic_callback_dropdown_region",
                            options=[
                                {"label": x, "value": x}
                                for x in sorted(df["Region"].unique())
                            ],
                            multi=True,
                        ),
                        html.Label("Ship Date"),
                        dcc.DatePickerRange(
                            id="offCanvas_icicle-x-my-date-picker-range",
                            min_date_allowed=min(df["ship_date"]),
                            max_date_allowed=max(df["ship_date"]),
                            end_date=max(df["ship_date"]),
                            start_date=min(df["ship_date"]),
                            clearable=True,
                        ),
                    ],
                    id="offCanvas_icicle-x-offcanvas",
                    title="Filters",
                    is_open=False,
                ),
            ]
        ),
        dcc.Graph(id="offCanvas_icicle-x-line_chart", className="mt-2 mb-4"),
    ],
    fluid=True,
)


@callback(
    Output("offCanvas_icicle-x-line_chart", "figure"),
    Input("offCanvas_icicle-x-dynamic_callback_dropdown_region", "value"),
    Input("offCanvas_icicle-x-my-date-picker-range", "start_date"),
    Input("offCanvas_icicle-x-my-date-picker-range", "end_date"),
)
def line_chart(region, start_date, end_date):
    dff = df.copy()

    if region is not None and len(region) > 0:
        dff = dff.query("Region == @region")

    if start_date is not None:
        dff = dff.query("ship_date > @start_date")

    if end_date is not None:
        dff = dff.query("ship_date < @end_date")

    dff = dff.drop(columns=['ship_date'])
    dff = dff.groupby(by=["Segment", "Region"]).sum().reset_index()

    fig = px.icicle(
        dff, path=[px.Constant("all"), "Segment", "Region"], values="profit_derived"
    )
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

    return fig


@callback(
    Output("offCanvas_icicle-x-offcanvas", "is_open"),
    Input("offCanvas_icicle-x-open-offcanvas", "n_clicks"),
    State("offCanvas_icicle-x-offcanvas", "is_open"),
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server()
