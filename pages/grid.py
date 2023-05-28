import dash

from lib.code_and_show import example_app


dash.register_page(__name__, description="Use of AG Grid with callback on cell click. This app uses top-down layout with regular-callback.")

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:  
- [AG Grid](https://dash.plotly.com/dash-ag-grid)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)
"""

layout = example_app(filename, notes=notes)
