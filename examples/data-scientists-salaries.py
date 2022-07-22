### Imports
from dash import Dash, dcc, html, Input, Output, no_update
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
import numpy as np
import pandas as pd

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/salaries-ai-jobs-net.csv"
)

app.layout = dbc.Container(
    # Creating the side by side layout
    dbc.Row(
        [
            dbc.Col(
                [
                    html.H3("Select columns"),
                    dcc.RadioItems(
                        options=[
                            {"label": i, "value": i}
                            for i in ["salary_in_usd", "remote_ratio"]
                        ],
                        value="remote_ratio",
                        id="data-scientists-salaries-x-checklist",
                        inline=False,
                    ),
                    html.Hr(),
                    html.H3("Select visualization type"),
                    dcc.RadioItems(
                        options=[
                            {"label": i, "value": i}
                            for i in ["Choropleth", "Bar", "Line"]
                        ],
                        value="Choropleth",
                        id="data-scientists-salaries-x-graphtype",
                        inline=False,
                    ),
                ],
                width=2,
            ),
            dbc.Col(
                [
                    html.H3("Graph for your selection"),
                    dcc.Graph(id="data-scientists-salaries-x-graph"),
                ],
                width=10,
            ),
        ]
    )
)


@app.callback(
    Output("data-scientists-salaries-x-graph", "figure"),
    [
        Input("data-scientists-salaries-x-checklist", "value"),
        Input("data-scientists-salaries-x-graphtype", "value"),
    ],
)
def show_figure(selected_cols, selected_graph_type):
    vf = df.copy()
    country_names_conv = pd.read_csv(
        "https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv"
    )
    vf = vf.merge(
        country_names_conv,
        how="inner",
        left_on=["company_location"],
        right_on="alpha-2",
    )
    if selected_graph_type == "Choropleth":
        fig = px.choropleth(
            vf,
            locations="alpha-3",
            color=selected_cols,
            hover_name="company_location",
            hover_data=[selected_cols, "name"],
        )
    elif selected_graph_type == "Bar":
        fig = px.bar(vf, x="company_location", y=selected_cols, color=selected_cols)
    elif selected_graph_type == "Line":
        fig = px.line(vf, x="company_location", y=selected_cols, color=selected_cols)

    return fig