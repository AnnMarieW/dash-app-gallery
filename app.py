import dash
from dash import Dash, html, dcc, Input, Output, State, ctx
import dash_bootstrap_components as dbc
from lib.utils import example_apps, example_source_codes, file_name_from_path
from lib.code_and_show import make_code_div

# syntax highlighting light or dark
light_hljs = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/styles/stackoverflow-light.min.css"
dark_hljs = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/styles/stackoverflow-dark.min.css"


app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.SPACELAB, dark_hljs, dbc.icons.BOOTSTRAP],
    # suppress_callback_exceptions=True,
)
server = app.server


for k in example_apps:
    if not k.startswith("error"):
        new_callback_map = example_apps[k].callback_map
        new_callback_list = example_apps[k]._callback_list

        app.callback_map.update(new_callback_map)
        app._callback_list.extend(new_callback_list)


fullscreen_modal = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle("Full screen")),
        dbc.ModalBody(id="content-fs"),
    ],
    id="modal-fs",
    fullscreen=True,
)

navbar = dbc.NavbarSimple(
    [
        dbc.Button("Overview", id="overview", href=dash.get_relative_path("/"), color="secondary", size="sm",className="ms-2"),
        dbc.Button("Index", href=dash.get_relative_path("/example-index"), color="secondary", size="sm", className="ms-2"),

         dbc.Button(
            "Dash Docs",
            id="dash-docs",
            href="https://dash.plotly.com/",
            target="_blank",
            color="secondary",
            size="sm",
            className="ms-2",
        ),
        dbc.Button("Fullscreen App", id="open-fs-app", color="secondary", size="sm"),
        dbc.Button("Fullscreen Code", id="open-fs-code", color="secondary", size="sm"),
    ],
    brand="Dash Example Index",
    brand_href=dash.get_relative_path("/"),
    color="primary",
    dark=True,
    fixed="top",
    className="mb-2 fs-3",
)

footer = html.H4(
    [
        dcc.Link(
            " Thank you contributors!",
            className="bi bi-github",
            href="https://github.com/AnnMarieW/dash-app-gallery/graphs/contributors",
            target="_blank",
        )
    ],
    className="p-4 mt-5 text-center",
)


app.layout = html.Div(
    [
        navbar,
        fullscreen_modal,
        dbc.Container(dash.page_container, fluid=True, style={"marginTop": "4rem"}),
        footer,
        dcc.Location(id="url", refresh=True),
    ]
)


@app.callback(
    Output("open-fs-app", "className"),
    Output("open-fs-code", "className"),
    Input("url", "pathname"),
)
def fullscreen(path):
    """Don't show fullscreen buttons on home page (gallery overview or index page or on error pages)"""

    if path in [dash.get_relative_path("/"), dash.get_relative_path("/example-index")]:
        return "d-none", "d-none"
    if path.startswith(dash.get_relative_path("/")+"error"):
        return "d-none", "d-none"
    return "ms-2", "ms-2"


@app.callback(
    Output("modal-fs", "is_open"),
    Output("content-fs", "children"),
    Input("open-fs-app", "n_clicks"),
    Input("open-fs-code", "n_clicks"),
    State("modal-fs", "is_open"),
    State("url", "pathname"),
)
def toggle_modal(n_app, n_code, is_open, pathname):
    filename = file_name_from_path(pathname)
    layout = None
    code = None
    if filename in example_apps:
        layout = example_apps[filename].layout
        code = example_source_codes[filename].replace(filename + "-x-", "")
        code = make_code_div(code)
    content = layout if ctx.triggered_id == "open-fs-app" else code

    if n_app or n_code:
        return not is_open, content
    return is_open, content

#
# @app.callback(
#     Output("url", "href"), Input("modal-fs", "is_open"), State("url", "pathname")
# )
# def refresh_page(is_open, pathname):
#     """refreshes screen when fullscreen mode is closed, else callbacks don't fire"""
#     if is_open is None:
#         return dash.no_update
#     return pathname if not is_open else dash.no_update


if __name__ == "__main__":
    app.run_server(debug=True)
