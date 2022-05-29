import dash
from dash import html, dcc

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="This application shows the connections between a Datepicker and Alert.",
    layout_type="top-bottom",
    components_type=["markdown", "datepicker", "alert", "button"],
    graph_type=None,
    callback_type="general"
)

filename = __name__.split("pages.")[1]

# any notes will be displayed below the code-and-show page in a dcc.Markdown component
notes = """
#### Dash Components in App:
- [Markdown component](https://dash.plotly.com/dash-core-components/markdown)
- [DatePickerSingle component](https://dash.plotly.com/dash-core-components/datepickersingle)

#### 3rd-party Dash Bootstrap Components: 
- [Button component](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/button/ "This component was made by the community and not officially maintained by Plotly.")
- [Alert component](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/alert/ "This component was made by the community and not officially maintained by Plotly.")

### Contributed by:
This example app was contributed by [someshfengde](https://github.com/someshfengde)

"""

layout = example_app(filename, notes=notes)
