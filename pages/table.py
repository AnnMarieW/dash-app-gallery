import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Use of DataTable with callback on cell click. This app uses top-down layout with regular callback.")

filename = __name__.split("pages.")[1]

notes = """
#### Dash components in App:  
- [DataTable component](https://dash.plotly.com/datatable)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)
"""

layout = example_app(filename, notes=notes)
