import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__, description="This app shows interactive network graph with Dash Cytoscape. It has a top-bottom layout and a regular-callback."
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:
- [Cytoscape](https://dash.plotly.com/cytoscape)
- [Dropdown](https://dash.plotly.com/dash-core-components/dropdown)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)
"""


layout = example_app(filename, notes=notes)
