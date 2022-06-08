import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="This application includes an example of 3d line chart.",
    layout_type="top-bottom",
    components_type=["dropdown", "line-3d", "card"],
    graph_type=None,
    callback_type="general",
)

filename = __name__.split("pages.")[1]

# any notes will be displayed below the code-and-show page in a dcc.Markdown component
notes = """
#### Dash Components in App:
- [3d-Line component](https://plotly.com/python/3d-line-plots/)
- [Dropdown component](https://plotly.com/python/dropdowns/)
#### Community Components:
Dash Bootstrap Components 
- [Layout component](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/ "This component was made by the community and not officially maintained by Plotly.")
- [Card component](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/ "This component was made by the community and not officially maintained by Plotly.")
##### Contributed by:
This example app was contributed by [tolgahancepel](https://github.com/tolgahancepel)
"""

layout = example_app(filename, notes=notes)