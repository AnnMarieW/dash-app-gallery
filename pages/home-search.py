import dash
from dash import html, callback, Output, Input, ALL, ctx
import dash_bootstrap_components as dbc
from utils.search import search_code_files
from utils.card_grid import make_card_grid
from utils.feature_app import feature_app_div


dash.register_page(
    __name__, name="Home - Overview", description="Dash App Gallery", path="/"
)


case_sensitive = (
    dbc.Switch(
        id="home-search-x-case-sensitive",
        label="Aa",
        value=False,
    ),
)
search_code_div = html.Div(
    [
        dbc.Label("Search code", className="fw-bolder"),
        dbc.InputGroup(
            [
                dbc.Input(
                    id="home-search-x-code-search-input",
                    debounce=True,
                ),
                dbc.InputGroupText(
                    case_sensitive, id="home-search-x-case-label", className="px-1"
                ),
            ]
        ),
        # dbc.Tooltip(
        #     "Find app examples with selected code, for example, try entering dcc.Dropdown, or scatter",
        #     target="home-search-x-code-search-input",
        # ),
        dbc.Tooltip(
            "Match Case",
            target="home-search-x-case-label",
        ),
    ],
    className="mb-2",
)

textbox_card = dbc.Card(
    ["Welcome to the Dash app gallery!"],
    style={"height": 225},
    className="shadow-sm p-4 mt-4 mx-2",
)


def filtered_registry(filtered_example_app_list):
    """
    Returns a filtered dash.page_registry dict based on a list of example app names
    """

    # We use the module param to filter the dash_page_registry
    # Note that the module name includes the pages folder name eg: "pages.bar-charts"
    filtered_registry = []
    for page in dash.page_registry.values():
        filename = page["module"].split("pages.")[1]
        if filename in filtered_example_app_list:
            filtered_registry.append(page)
    return filtered_registry


layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col([search_code_div, feature_app_div], className="m-2"),
                dbc.Col(textbox_card),
            ]
        ),
        dbc.Row(dbc.Col(html.Div(id="home-search-x-grid"))),
    ],
    className="p-4 mx-2",
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

    # show apps based on search field
    if input_id == "home-search-x-code-search-input":
        if searchterms:
            filtered_example_app_names = search_code_files(searchterms, case_sensitive)
            registry = filtered_registry(filtered_example_app_names)
            return make_card_grid(registry=registry), dash.no_update, dash.no_update

    # show feature apps
    if isinstance(input_id, dict):
        # The searchterms are from the "index" key of the pattern matching dict id
        # See `utils.feature_app.py for more details.
        searchterms = input_id["index"]
        case_sensitive = True
        filtered_example_app_names = search_code_files(searchterms, case_sensitive)
        registry = filtered_registry(filtered_example_app_names)
        return make_card_grid(registry=registry), None, dash.no_update

    if input_id == "overview":
        # close the featured apps accordian when the overview button is clicked.
        return make_card_grid(registry=registry), None, None

    return make_card_grid(registry=registry), None, None
