import dash
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import dash_labs as dl
from utils.init_app import example_apps

# syntax highlighting light or dark
light_hljs = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/styles/stackoverflow-light.min.css"
dark_hljs = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/styles/stackoverflow-dark.min.css"


app = Dash(
    __name__,
    plugins=[dl.plugins.pages],
    external_stylesheets=[dbc.themes.SPACELAB, dark_hljs],
    suppress_callback_exceptions=True,
)


for k in example_apps:
    # Prepend to layout IDs recursively in-place
    new_callback_map = example_apps[k].callback_map
    new_callback_list = example_apps[k]._callback_list

    app.callback_map.update(new_callback_map)
    app._callback_list.extend(new_callback_list)


navbar = dbc.NavbarSimple(
    [
        dbc.Button("Overview", href="/", color="secondary"),
        dbc.Switch(
            id="full-screen",
            label="Full Screen",
            value=False,
            label_class_name="text-white",
            className="d-none",  # todo hidden for now
        ),
    ],
    brand="Dash App Gallery",
    color="primary",
    dark=True,
    fixed="top",
    className="mb-2",
)


app.layout = html.Div(
    [
        navbar,
        dbc.Container(
            dl.plugins.page_container, fluid=True, style={"marginTop": "4rem"}
        ),
        dcc.Location(id="url"),
    ]
)


@app.callback(Output("full-screen", "className"), Input("url", "pathname"))
def fullscreen(path):
    if path == "/":
        return "d-none"
    # return "ms-2 mt-2"  # todo hidden for now until the swtich works
    return "d-none"


if __name__ == "__main__":
    app.run_server(debug=True)
