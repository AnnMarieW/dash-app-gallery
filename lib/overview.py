"""
This is the home page which displays an overview of the card grid which shows a preview of the components and examples
"""

import dash
from dash import html, callback, Output, Input, ALL, ctx
import dash_bootstrap_components as dbc
from lib.utils import filter_registry
from lib.card_grid import make_card_grid
from lib.feature_app import feature_app_div
import lib.overview_textbox


def make_search_code_div(code_filter):
    case_sensitive = (
        dbc.Switch(
            id="home-search-x-case-sensitive",
            label="Aa",
            value=False,
            style={'paddingTop': 'inherit'}
        ),
    )

    return html.Div(
        [
            dbc.InputGroup(
                [
                    dbc.InputGroupText(
                        html.I(className="bi bi-search"),
                    ),
                    dbc.Input(id="home-search-x-code-search-input", value=code_filter),
                    dbc.InputGroupText(
                        case_sensitive, id="home-search-x-case-label"
                    ),
                ]
            ),
            dbc.Tooltip(
                "Match Case",
                target="home-search-x-case-label",
            ),
        ],
        className="mb-2",
    )


def layout(code=None, **other):
    """
    Displays the apps in a card grid.
    May pass query stings to filter the examples.
    If using query strings, the variable name must be `code`.  eg `http://127.0.0.1:8050/?code=dropdown`
    """
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [make_search_code_div(code), feature_app_div], md=6, className="py-4"
                    ),
                    dbc.Col(lib.overview_textbox.card, md=6, className="py-4"),
                ], className='align-items-center'
            ),
            dbc.Row(dbc.Col(html.Div(id="home-search-x-grid"))),
        ],
        className="p-2",
    )


@callback(
    Output("home-search-x-grid", "children"),
    Output("home-search-x-code-search-input", "value"),
    Output("featured-apps", "active_item"),
    Input("home-search-x-code-search-input", "value"),
    Input("home-search-x-case-sensitive", "value"),
    Input({"type": "feature_app", "index": ALL}, "n_clicks"),
    Input("overview", "n_clicks"),
)
def update(searchterms, case_sensitive, feature_app, overview):
    input_id = ctx.triggered_id
    registry = dash.page_registry.values()

    # show feature apps
    if isinstance(input_id, dict):
        # The searchterms are from the "index" key of the pattern matching dict id
        # See `utils.feature_app.py for more details.
        searchterms = input_id["index"]
        case_sensitive = True
        registry = filter_registry(searchterms, case_sensitive)
        return make_card_grid(registry=registry), None, dash.no_update

    if input_id == "overview":
        # close the featured apps accordian when the overview button is clicked.
        return make_card_grid(registry=registry), None, None

    if searchterms:
        registry = filter_registry(searchterms, case_sensitive)
        return make_card_grid(registry=registry), dash.no_update, dash.no_update

    return make_card_grid(registry=registry), None, None
