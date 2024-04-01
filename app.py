import dash
from dash import Dash, html, dcc, Input, Output, State, ctx
import dash_bootstrap_components as dbc
from whitenoise import WhiteNoise
from lib.utils import example_apps, example_source_codes, file_name_from_path
from lib.code_and_show import make_code_div

# syntax highlighting light or dark
light_hljs = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/styles/stackoverflow-light.min.css"
dark_hljs = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/styles/stackoverflow-dark.min.css"

logo = "https://user-images.githubusercontent.com/72614349/182969599-5ae4f531-ea01-4504-ac88-ee1c962c366d.png"
logo_dark = "https://user-images.githubusercontent.com/72614349/182967824-c73218d8-acbf-4aab-b1ad-7eb35669b781.png"

# for vis-timeline example
vis_timeline_css = 'https://unpkg.com/vis-timeline@latest/styles/vis-timeline-graph2d.min.css'
vis_timeline_script = 'https://unpkg.com/vis-timeline@latest/standalone/umd/vis-timeline-graph2d.min.js'

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.SPACELAB, dark_hljs, dbc.icons.BOOTSTRAP, vis_timeline_css],
    external_scripts=[vis_timeline_script],
    suppress_callback_exceptions=True
)
server = app.server
server.wsgi_app = WhiteNoise(server.wsgi_app, root="assets/")


for k in example_apps:
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

btn_group = html.Div([
        dbc.Button(
            "Home",
            id="overview",
            href=dash.get_relative_path("/"),
            color='primary',
            outline=True,
            className='mt-2 mt-md-0 me-md-2'
        ),
        dbc.Button(
            "Dash Docs",
            id="dash-docs",
            href="https://dash.plotly.com/",
            target="_blank",
            color='primary',
            outline=True,
            className='text-nowrap mt-2 mt-md-0'
        ),
        dbc.Button(
            "Fullscreen App", 
            id="open-fs-app",
            color='primary',
            outline=True,
        ),
        dbc.Button(
            "Fullscreen Code", 
            id="open-fs-code",
            color='primary',
            outline=True,
        ),
], className='navbar-nav')


navbar = dbc.Navbar([
    dbc.Container([
        html.A([
            html.Img(src=logo, height=40, width=40, className='align-middle me-2'),
            html.Span('Dash Example Index',
                        className='d-none d-lg-inline-block align-middle'
                        ),
            html.Span('Example Index', className='d-lg-none align-middle')
        ], href='/', className='navbar-brand fw-bold'),
        
        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
        dbc.Collapse([
            html.Div(className='me-auto'), btn_group],
            id="navbar-collapse",
            is_open=False,
            navbar=True
        )
    ], fluid=True)
])


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
        dbc.Container(dash.page_container, fluid=True),
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
    """Don't show fullscreen buttons on home page (gallery overview)"""

    if path == dash.get_relative_path("/"):
        return "d-none", "d-none"
    return "text-nowrap ms-md-2 mt-2 mt-md-0 me-md-2", "text-nowrap mt-2 mt-md-0 me-md-2"


# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

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


@app.callback(
    Output("url", "href"), Input("modal-fs", "is_open"), State("url", "pathname")
)
def refresh_page(is_open, pathname):
    """refreshes screen when fullscreen mode is closed, else callbacks don't fire"""
    if is_open is None:
        return dash.no_update
    return pathname if not is_open else dash.no_update


if __name__ == "__main__":
    app.run_server(debug=True, port='8050')
