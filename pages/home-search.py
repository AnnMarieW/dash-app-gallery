import dash
from dash import html, dcc, callback, Output, Input
import uuid
import random
import dash_bootstrap_components as dbc

rd = random.Random(0)

dash.register_page(__name__, description="Sample Dash Apps", path="/")


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
                        html.Img(src=dash.get_asset_url(page["image"]), height=200),
                        href=page["path"],
                        id=tooltip_id,
                    ),
                    html.P(
                        page["description"],
                        className="card-text",
                    ),
                ]
            ),
            dbc.Tooltip(page["description"], target=tooltip_id),
        ]
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


def layout():
    return html.Div(
        [
            "Select Callback Structure:",
            dcc.Dropdown(
                ["All", "1 Output 1 Input", "1 Output 2 Input"],
                "All",
                clearable=False,
                id="home-search-x-dd",
                className="mb-4",
                persistence=True,
            ),
            "Select Graph Type:",
            dcc.Dropdown(["All", "To Do"], "All", clearable=False, className="mb-4"),
            html.Div(id="home-search-x-grid"),
        ]
    )


@callback(
    Output("home-search-x-grid", "children"),
    Input("home-search-x-dd", "value"),
)
def update(value):
    if value == "All":
        registry = dash.page_registry.values()
    else:
        registry = [
            p for p in dash.page_registry.values() if p.get("callback_dd") == value
        ]

    return make_card_grid(registry=registry)
