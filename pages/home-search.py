import dash
from dash import html, dcc, callback, Output, Input, callback_context as ctx
import dash_bootstrap_components as dbc
from utils.search_code import search_code_files
from utils.card_grid import make_card, make_card_grid


dash.register_page(
    __name__, name="Home - Overview", description="Dash App Gallery", path="/"
)


callback_structure_div = html.Div(
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
    ]
)

graph_types_div = html.Div(
    [
        "Select Graph Type:",
        dcc.Dropdown(
            ["All", "To Do"], "All", clearable=False, className="mb-4", persistence=True
        ),
    ]
)


search_code_div = html.Div(
    [
        "Search code files",
        dbc.Input(id="home-search-x-code-search-input", debounce=True),
        dbc.Tooltip(
            "Find app examples with selected code, for example, try entering dcc.Dropdown, or scatter",
            target="home-search-x-code-search-input",
        ),
    ]
)



def layout():
    return html.Div(
        [
            dbc.Row([dbc.Col(search_code_div), dbc.Col(callback_structure_div)]),
            dbc.Row(dbc.Col(html.Div(id="home-search-x-grid"))),
        ]
    )


@callback(
    Output("home-search-x-grid", "children"),
    Output("home-search-x-code-search-input", "value"),
    Output("home-search-x-dd", "value"),
    Input("home-search-x-code-search-input", "value"),
    Input("home-search-x-dd", "value"),
)
def update(searchterms, dd_value):
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    registry = dash.page_registry.values()

    if input_id == "home-search-x-code-search-input":
        if searchterms:
            filtered_example_app_names = search_code_files(searchterms)
            # We use the module param to filter the dash_page_registry
            # Note that the module name includes the pages folder name eg: "pages.bar-charts"
            print("filtered", filtered_example_app_names)
            registry = []
            for page in dash.page_registry.values():
                filename = page["module"].split("pages.")[1]
                if filename in filtered_example_app_names:
                    registry.append(page)
            print("reg", registry)
            return make_card_grid(registry=registry), dash.no_update, "All"

    if input_id == "home-search-x-dd":
        if dd_value != "All":
            registry = [
                p
                for p in dash.page_registry.values()
                if p.get("callback_dd") == dd_value
            ]
            return make_card_grid(registry=registry), None, dash.no_update

    return make_card_grid(registry=registry), None, "All"
