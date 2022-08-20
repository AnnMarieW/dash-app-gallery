from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from . import callbacks, components, figures, layouts, hello_world


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
    # make_card("Side-by-side Layouts - Dash Bootstrap", layouts.side_by_side_dbc),
    # make_card("Side-by-side Layouts - Dash Enterprise", layouts.side_by_side_ddk),
    # make_card("Callbacks - Declared IDs", callbacks.declared_id),
    make_card("Callbacks - Randomly Generated IDs", callbacks.generated_id),
    make_card("Callbacks - Multiple Outputs/Inputs", callbacks.multiple),
    make_card("Basic Figures", figures.basic),
    make_card("Statistical Figures", figures.statistical),
    make_card("Scientific Figures", figures.scientific),
    make_card("Maps", figures.maps),
]


def make_card_grid(cards_per_row=2, registry=None):
    # if registry is None:
    #     registry = dash.page_registry.values()
    row = []
    grid = []
    for card in cards:
        #  if page["relative_path"] != dash.get_relative_path("/"):
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
