# Imports
from tkinter import Button
from turtle import width
from dash import Dash, dcc, html, Input, Output, no_update, State
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
import numpy as np
import pandas as pd

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                html.Div(
                    html.Img(
                        src="./assets/flames.png",
                        style={"width": "100%", "height": "50%"},
                    ),
                    style={"width": "100%", "height": "50%"},
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown("## **Enter your first name**"),
                        dcc.Input(
                            id="flames-x-name",
                            value="",
                            type="text",
                            style={"width": "100%"},
                            placeholder="Enter your First name",
                        ),
                    ],
                    width=6,
                ),
                dbc.Col(
                    [
                        dcc.Markdown("## **Enter your crush's name** "),
                        dcc.Input(
                            id="flames-x-crush",
                            value="",
                            type="text",
                            placeholder="Enter your crush's name",
                            style={"width": "100%"},
                        ),
                    ],
                    width=6,
                ),
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Button(
                    "💘 Calculate Flames 💘", id="flames-x-submit-button", color="primary"
                )
            ]
        ),
        dbc.Modal(
            id="flames-x-modal",
            size="lg",
        ),
    ],
    fluid=True,
    className="dbc",
)


@app.callback(
    [Output("flames-x-modal", "is_open"), Output("flames-x-modal", "children")],
    [Input("flames-x-submit-button", "n_clicks")],
    [State("flames-x-name", "value"), State("flames-x-crush", "value")],
)
def flames_x_modal(n_clicks, name, crush):
    name = name.strip().lower()
    crush = crush.strip().lower()
    name_count = {}
    crush_count = {}
    flames_count = 0
    for x in name:
        if name_count.__contains__(x):
            name_count[x] += 1
        else:
            name_count[x] = 1
    for x in crush:
        if crush_count.__contains__(x):
            crush_count[x] += 1
        else:
            crush_count[x] = 1
    already_done = []
    for x, nam_count in name_count.items():
        if crush_count.__contains__(x):
            already_done.append(x)
            min_f = min(name_count[x], crush_count[x])
            max_f = max(name_count[x], crush_count[x])
            flames_count += min_f + (max_f - min_f)
        else:
            flames_count += name_count[x]
    for x, cru_count in crush_count.items():
        if x not in already_done:
            flames_count += crush_count[x]
    flames = [
        "👬 Friends 👬",
        "💘 Love 💘",
        "💝 Affection 💝",
        "💍 Marriage 💍",
        "👿 Enemy 👿",
        "👬 Siblings 👬",
    ]

    who_is_it = flames[(flames_count) // 6]

    children = dbc.Container(
        [
            dbc.ModalHeader(
                dbc.ModalTitle("What did flames theory says 🤫."), close_button=True
            ),
            dbc.ModalBody(
                [
                    html.H3(f"{name} and {crush} are {who_is_it}"),
                    html.Img(
                        src="./assets/love.gif",
                        style={"width": "100%", "height": "50%"},
                    ),
                ]
            ),
        ],
    )

    if n_clicks:
        return [True, children]

    return [False, no_update]


if __name__ == "__main__":
    app.run_server(debug=True)
