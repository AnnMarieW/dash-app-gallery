import dash
from dash import html
import uuid
import random
import dash_bootstrap_components as dbc

rd = random.Random(0)


def make_card(page):
    tooltip_id = str(uuid.UUID(int=rd.randint(0, 2 ** 128)))
    return dbc.Card(
        [
            dbc.CardHeader(
                [
                    dbc.NavLink(
                        page["title"],
                        href=page["path"],
                    ),
                ]
            ),
            dbc.CardBody(
                [
                    html.A(
                        html.Div(
                            html.Img(
                                src=dash.get_asset_url(page["image"]),
                                className="img-fluid",
                            ),
                        ),
                        href=page["path"],
                        id=tooltip_id,
                    ),

                    html.P(
                        page["description"],
                        className="card-text p-2 border-top",
                    ),
                ]
            ),
            dbc.Tooltip(page["description"], target=tooltip_id),
        ],
        className="m-2 shadow ",
    )


def make_card_grid(cards_per_row=3, registry=None):
    if registry is None:
        registry = dash.page_registry.values()
    row = []
    grid = []
    for page in registry:
        if page["path"] != "/":
            if len(row) < cards_per_row:
                row.append(make_card(page))
            if len(row) == cards_per_row:
                grid.append(dbc.CardGroup(row, className="mb-4"))
                row = []
    grid.append(dbc.CardGroup(row))
    return grid
