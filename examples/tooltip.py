from dash import Dash, dcc, html, Input, Output, no_update
import pandas as pd
import plotly.express as px

# Reading data
df = pd.read_table(
    "https://raw.githubusercontent.com/plotly/datasets/master/global_super_store_orders.tsv"
)

# Transforming column types so that datetime functions can be applied correctly
df["Order Date"] = pd.to_datetime(df["Order Date"], format='%m/%d/%y')
df["Profit"] = df["Profit"].str.replace(",", ".")
df["Profit"] = df["Profit"].astype("float")


# Transforming 'Order Date' column into yyyy-mm format
df["year_month"] = pd.DatetimeIndex(df["Order Date"]).to_period("M").astype(str)

# Grouping data as per 'Order Date' dimension.
# Getting time series - profit per month.
df_grouped = (
    df[["Order Date", "Profit"]]
    .groupby(by=pd.Grouper(key="Order Date", axis=0, freq="ME"))
    .sum()
    .reset_index()
)

# Creating base bar chart.
# Why 'base'? --> Because it will be shown on page all the time.
# Below there is one bar chart that will be shown only on hover.
fig = px.bar(data_frame=df_grouped, x="Order Date", y="Profit", template="simple_white")

fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# turn off native plotly.js hover effects - make sure to use
# hoverinfo="none" rather than "skip" which also halts events.
fig.update_traces(hoverinfo="none", hovertemplate=None)


app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Dash Tooltip Example", style={"textAlign": "center"}),
        # Base bar chart i.e. bar chart that will always be shown on map.
        dcc.Graph(id="tooltip-graph-basic-2", figure=fig, clear_on_unhover=True),
        # Component that will be updated when on hover.
        # Here will come graph created in display_hover callback function.
        dcc.Tooltip(id="tooltip-graph", direction="left"),
    ]
)


@app.callback(
    Output("tooltip-graph", "show"),
    Output("tooltip-graph", "bbox"),
    Output("tooltip-graph", "children"),
    Input("tooltip-graph-basic-2", "hoverData"),
)
def display_hover(hover_data):

    # Do not show tooltip popup window if mouse is not hovered over
    if hover_data is None:
        return False, no_update, no_update

    # print(hover_data)
    # Here we are getting data about X-axis of hovered bar chart
    # i.e. we are interested in date of hovered bar.
    x = hover_data["points"][0]["x"]

    # Here we are filtering first 7 digits of date value.
    # Why first 7? --> Because we want to have year and month.
    # In day we are not interested.
    date_month = x[:7]

    # Filtering initial DataFrame in order to get specific month.
    df_filtered = df.query(f"year_month == '{date_month}'")

    # Grouping data so that we have DataFrame grouped as per 'Segment' dimension.
    df_filtered_grouped = (
        df_filtered[["Segment", "Profit"]].groupby(by="Segment").sum().reset_index()
    )

    # Creating Plotly figure that will be shown in tooltip
    fig1 = px.bar(
        data_frame=df_filtered_grouped, x="Segment", y="Profit", template="simple_white"
    )
    fig1.update_layout(margin=dict(t=0, l=0, r=0, b=0))

    # Purpose of following two lines is to get info about bounding box i.e.
    # about coordinates of popup window/tooltip window that will be created.
    pt = hover_data["points"][0]
    bbox = pt["bbox"]

    children = [
        html.Div(
            [
                html.H4(f"Year-Month: {date_month}"),
                dcc.Graph(figure=fig1),
            ],
            style={"width": "200px", "height": "200px", "whiteSpace": "normal"},
        )
    ]

    return True, bbox, children


if __name__ == "__main__":
    app.run_server(debug=True)
