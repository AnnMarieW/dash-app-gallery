"""
Creates an app used by script to update the images.  Each page contains example app only with no navigation or headers.
Start this app, then run create_all_images.py or create_missing_images.py
"""


import dash
import dash_bootstrap_components as dbc
from lib.code_and_show import example_app, make_app_first
from lib.utils import file_names

from lib.utils import example_apps


# for vis-timeline example
vis_timeline_css = 'https://unpkg.com/vis-timeline@latest/styles/vis-timeline-graph2d.min.css'
vis_timeline_script = 'https://unpkg.com/vis-timeline@latest/standalone/umd/vis-timeline-graph2d.min.js'

app = dash.Dash(
    __name__,
    use_pages=True,
    pages_folder="",
    external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.BOOTSTRAP, vis_timeline_css],
    external_scripts=[vis_timeline_script],
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
        layout=example_app(page, show_code=False),
    )


app.layout = dbc.Container(dash.page_container, fluid=True, className="mt-2")


if __name__ == "__main__":
    app.run_server(debug=False)
