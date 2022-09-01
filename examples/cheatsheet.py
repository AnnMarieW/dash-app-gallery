from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from examples.cheatsheets import callbacks, components, figures, layouts, hello_world, share

app=Dash(__name__)


def make_card(header, content):
    return dbc.Card(
        [
            dbc.CardHeader(header, className="bg-secondary"),
            dcc.Markdown(content, style={"maxHeight": 450}, className="overflow-auto"),
        ],
        className="m-4 shadow text-white bg-black",
        style={
            "minWidth": "36rem",
        },
    )


cards = [
    make_card("Hello World", hello_world.hello),
    make_card("Common Components", components.common),
    make_card("Side-by-side Layouts", layouts.side_by_side),
    make_card("Callbacks - Randomly Generated IDs", callbacks.generated_id),
    make_card("Callbacks - Multiple Outputs/Inputs", callbacks.multiple),
    make_card("Callbacks - Which input triggered", callbacks.ctx),
    make_card("Share the App", share.deploy),
    make_card("Basic Figures", figures.basic),
    make_card("Statistical Figures", figures.statistical),
    make_card("Scientific Figures", figures.scientific),
    make_card("Maps", figures.maps),
]


def make_card_grid(cards_per_row=2):
    row = []
    grid = []
    for card in cards:
        if len(row) < cards_per_row:
            row.append(card)
        if len(row) == cards_per_row:
            grid.append(dbc.CardGroup(row, className="mb-4"))
            row = []
    grid.append(dbc.CardGroup(row))
    return grid


layout = dbc.Container(
    [
        html.H4("Dash Cheatsheet", className="text-center"),
        dbc.Row(dbc.Col(make_card_grid())),
    ],
    fluid=True,
)
