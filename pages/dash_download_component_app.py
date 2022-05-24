import dash
from dash import html, dcc

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app let's the user download datatable data as excel or csv files, using the dcc.Download component and a dropdown.",
    layout_type="top-bottom",
    components_type=["button", "dropdown", "datatable", "download"],
    graph_type="datatable",
    callback_type="general",
)

filename = __name__.split("pages.")[1]

# any notes will be displayed below the code-and-show page in a dcc.Markdown component
notes = """
### For more information see:
Dash docs:  

- [DataTable component](https://dash.plotly.com/datatable)
- [Button component](https://dash.plotly.com/dash-html-components/button)
- [Dropdown component](https://dash.plotly.com/dash-core-components/dropdown)
- [Download component](https://dash.plotly.com/dash-core-components/download)

### Contributed by:
This example app was contributed by [milanzmitrovic]https://github.com/milanzmitrovic)

"""

layout = example_app(filename, notes=notes)
