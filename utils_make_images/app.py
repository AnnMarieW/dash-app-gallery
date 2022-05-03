"""
Creates an app used by script to update the images.  Each page contains example app only with no navigation or headers.
Start this app, then run update_images_all.py or update_images_missing.py
"""


import dash
import dash_labs as dl
import dash_bootstrap_components as dbc
from utils.code_and_show import example_app, make_app_first
from utils.file_names import get_example_app_names

example_apps = get_example_app_names()


app = dash.Dash(
    __name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.SPACELAB],
)

for page in example_apps:
    dash.register_page(
        page,
        layout=example_app(
            f"pages/examples/{page}.py", show_code=False, make_layout=make_app_first
        ),
    )


app.layout = dbc.Container(dl.plugins.page_container, fluid=True, className="mt-2")


if __name__ == "__main__":
    app.run_server(debug=True)
