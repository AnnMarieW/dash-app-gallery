from dash import Dash, Input, Output, callback, dcc, html
import copy
import plotly.express as px
import pandas as pd

df = pd.read_table(
    "https://raw.githubusercontent.com/plotly/datasets/master/global_super_store_orders.tsv"
)

df["Order Date"] = pd.to_datetime(df["Order Date"], format='%m/%d/%y' )
df["Profit"] = df["Profit"].str.replace(",", ".")
df["Profit"] = df["Profit"].astype("float")

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H5("Region"),
        dcc.Dropdown(
            id="dynamic-callback-x-region", options=sorted(df["Region"].unique())
        ),
        html.H5("Country"),
        dcc.Dropdown(
            id="dynamic-callback-x-country",
            options=sorted(df["Country"].unique()),
            value=df["Country"][0],
        ),
        html.H5("State"),
        dcc.Dropdown(
            id="dynamic-callback-x-state",
            options=sorted(df["State"].unique()),
        ),
        html.Br(),
        dcc.Graph(id="dynamic-callback-x-line"),
    ]
)


@callback(
    Output("dynamic-callback-x-country", "options"),
    Input("dynamic-callback-x-state", "value"),
    Input("dynamic-callback-x-region", "value"),
)
def chained_callback_country(state, region):

    dff = copy.deepcopy(df)

    if state is not None:
        dff = dff.query("State == @state")

    if region is not None:
        dff = dff.query("Region == @region")

    return sorted(dff["Country"].unique())


@callback(
    Output("dynamic-callback-x-state", "options"),
    Input("dynamic-callback-x-country", "value"),
    Input("dynamic-callback-x-region", "value"),
)
def chained_callback_state(country, region):

    dff = copy.deepcopy(df)

    if country is not None:
        dff = dff.query("Country == @country")

    if region is not None:
        dff = dff.query("Region == @region")

    return sorted(dff["State"].unique())


@callback(
    Output("dynamic-callback-x-region", "options"),
    Input("dynamic-callback-x-country", "value"),
    Input("dynamic-callback-x-state", "value"),
)
def chained_callback_region(country, state):

    dff = copy.deepcopy(df)

    if country is not None:
        dff = dff.query("Country == @country")

    if state is not None:
        dff = dff.query("State == @state")

    return sorted(dff["Region"].unique())


@callback(
    Output("dynamic-callback-x-line", "figure"),
    Input("dynamic-callback-x-country", "value"),
    Input("dynamic-callback-x-state", "value"),
    Input("dynamic-callback-x-region", "value"),
)
def line_chart(country, state, region):

    dff = copy.deepcopy(df)

    if country is not None:
        dff = dff.query("Country == @country")

    if state is not None:
        dff = dff.query("State == @state")

    if region is not None:
        dff = dff.query("Region == @region")

    grouped_df = dff.groupby(dff["Order Date"]).sum().reset_index()

    fig = px.line(
        x=grouped_df["Order Date"],
        y=grouped_df["Profit"],
        template="simple_white",
        labels={"x": "Order Date", "y": "Profit"},
    )

    return fig


if __name__ == "__main__":
    app.run()
