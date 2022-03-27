import uuid
import random
import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash_labs as dl

rd = random.Random(0)

# syntax highlighting
light_hljs = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/styles/stackoverflow-light.min.css"
dark_hljs = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/styles/stackoverflow-dark.min.css"

app = Dash(
    __name__,
    plugins=[dl.plugins.pages],
    external_stylesheets=[dbc.themes.SPACELAB, light_hljs],
    suppress_callback_exceptions=True,
)

topbar = html.H2(
    "Dash App Gallery",
    className="p-4 bg-primary text-white ",
)


def make_navlink_with_tooltip(page):
    tooltip_id = str(uuid.UUID(int=rd.randint(0, 2 ** 128)))
    return html.Div(
        [
            dbc.NavLink(
                [
                    html.Div(page["name"], className="ms-2"),
                ],
                href=page["path"],
                active="exact",
                id=tooltip_id,
            ),
            dbc.Tooltip(page["description"], target=tooltip_id, placement="top"),
        ]
    )


sidebar = dbc.Card(
    [
        dbc.NavLink(
            [
                html.Div("Home", className="ms-2"),
            ],
            href="/",
            active="exact",
        ),
        html.H6("Sample Apps", className="mt-2"),
        dbc.Nav(
            [
                make_navlink_with_tooltip(page)
                for page in dash.page_registry.values()
                if page["path"] != "/"
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="overflow-auto sticky-top",
    style={"maxHeight": 600},
)

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                topbar,
                dbc.Col(sidebar, width=3, lg=2),
                dbc.Col(dl.plugins.page_container, width=8, lg=10),
            ]
        ),
    ],
    fluid=True,
)


if __name__ == "__main__":
    app.run_server(debug=True)

