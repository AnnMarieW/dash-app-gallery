import dash
from dash import html, dcc

from utils.code_and_show import example_app, make_app_first


dash.register_page(
    __name__,
    description="application showing usage for Datepicker and alert.",
    layout_type="top-bottom",
    graph_type=None,
    callback_type="general",
)

filename = __name__.split("pages.")[1]

# any notes will be displayed below the code-and-show page in a dcc.Markdown component
notes = """
### This application uses dash-bootstrap-components and dash-mantine-components
components used : 
    dbc.Alert()
    dmc.DatePicker()

### Contributed by:
This example app was contributed by [someshfengde](https://github.com/someshfengde)

"""

layout = example_app(filename, notes=notes)
