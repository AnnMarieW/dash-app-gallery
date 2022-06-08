from dash import Dash, Input, Output, callback, dcc, html
import copy
import plotly.express as px
import pandas as pd

df = pd.read_table(
    "https://raw.githubusercontent.com/plotly/datasets/master/global_super_store_orders.tsv"
)

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Profit"] = df["Profit"].str.replace(",", ".")
df["Profit"] = df["Profit"].astype("float")

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H5("Region"),
        dcc.Dropdown(
            id="dynamic-callback-x-region",
            options=[{"label": x, "value": x} for x in sorted(df["Region"].unique())],
        ),
        html.H5("Country"),
        dcc.Dropdown(
            id="dynamic-callback-x-country",
            options=[{"label": x, "value": x} for x in sorted(df["Country"].unique())],
            value=df["Country"][0],
        ),
        html.H5("State"),
        dcc.Dropdown(
            id="dynamic-callback-x-state",
            options=[{"label": x, "value": x} for x in sorted(df["State"].unique())],
        ),
        html.Br(),
        dcc.Graph(id="dynamic-callback-x-line"),
    ]
)


@callback(
    Output(component_id="dynamic-callback-x-country", component_property="options"),
    [
        Input(component_id="dynamic-callback-x-state", component_property="value"),
        Input(component_id="dynamic-callback-x-region", component_property="value"),
    ],
)
def chained_callback_country(state, region):

    dff = copy.deepcopy(df)

    if state is not None:
        dff = dff.query("State == @state")

    if region is not None:
        dff = dff.query("Region == @region")

    return [{"label": x, "value": x} for x in sorted(dff["Country"].unique())]


@callback(
    Output(component_id="dynamic-callback-x-state", component_property="options"),
    [
        Input(component_id="dynamic-callback-x-country", component_property="value"),
        Input(component_id="dynamic-callback-x-region", component_property="value"),
    ],
)
def chained_callback_state(country, region):

    dff = copy.deepcopy(df)

    if country is not None:
        dff = dff.query("Country == @country")

    if region is not None:
        dff = dff.query("Region == @region")

    return [{"label": x, "value": x} for x in sorted(dff["State"].unique())]


@callback(
    Output(component_id="dynamic-callback-x-region", component_property="options"),
    [
        Input(component_id="dynamic-callback-x-country", component_property="value"),
        Input(component_id="dynamic-callback-x-state", component_property="value"),
    ],
)
def chained_callback_region(country, state):

    dff = copy.deepcopy(df)

    if country is not None:
        dff = dff.query("Country == @country")

    if state is not None:
        dff = dff.query("State == @state")

    return [{"label": x, "value": x} for x in sorted(dff["Region"].unique())]


@callback(
    Output(component_id="dynamic-callback-x-line", component_property="figure"),
    [
        Input(component_id="dynamic-callback-x-country", component_property="value"),
        Input(component_id="dynamic-callback-x-state", component_property="value"),
        Input(component_id="dynamic-callback-x-region", component_property="value"),
    ],
)
def line_chart(country, state, region):

    dff = copy.deepcopy(df)

    if country is not None:
        dff = dff.query("Country == @country")

    if state is not None:
        dff = dff.query("State == @state")

    if region is not None:
        dff = dff.query("Region == @region")

    grouped_df = dff.groupby(dff["Order Date"].dt.week).sum().reset_index()

    fig = px.line(
        x=grouped_df["Order Date"],
        y=grouped_df["Profit"],
        template="simple_white",
        labels={"x": "Order Date", "y": "Profit"},
    )

    return fig


if __name__ == "__main__":
    app.run()
