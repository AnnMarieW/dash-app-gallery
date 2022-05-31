"""
Creates an app used by script to update the images.  Each page contains example app only with no navigation or headers.
Start this app, then run update_images_all.py or update_images_missing.py
"""


import dash
import dash_labs as dl
import dash_bootstrap_components as dbc
from utils.code_and_show import example_app, make_app_first
from utils.init_app import file_names

from utils.init_app import example_apps

app = dash.Dash(
    __name__,
    plugins=[dl.plugins.pages],
    external_stylesheets=[dbc.themes.SPACELAB],
)

for k in example_apps:
    # Prepend to layout IDs recursively in-place
    new_callback_map = example_apps[k].callback_map
    new_callback_list = example_apps[k]._callback_list

    app.callback_map.update(new_callback_map)
    app._callback_list.extend(new_callback_list)

for page in file_names:
    dash.register_page(
        page,
        layout=example_app(page, show_code=False, make_layout=make_app_first),
    )


app.layout = dbc.Container(dl.plugins.page_container, fluid=True, className="mt-2")


if __name__ == "__main__":
    app.run_server(debug=False)
