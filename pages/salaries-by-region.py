import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="This application includes an example of a 3d line chart with a dropdown.",
    layout_type="side by side",
    components_type=["dropdown"],
    graph_type="3D-Line",
    callback_type="general",
)

filename = __name__.split("pages.")[1]

# any notes will be displayed below the code-and-show page in a dcc.Markdown component
notes = """
#### Dash Components in App:
- [Dropdown component](https://dash.plotly.com/dash-core-components/dropdown)

#### Plotly Documentation:
- [3d-Line component](https://plotly.com/python/3d-line-plots/)

##### Contributed by:
This example app was contributed by [tolgahancepel](https://github.com/tolgahancepel)
"""

layout = example_app(filename, notes=notes)
