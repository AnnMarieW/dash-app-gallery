import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app connects between selected rows in Dash AG Grid to update traces of a parallel coordinates graph. It has a top-bottom layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [Dash AG Grid](https://dash.plotly.com/dash-ag-grid)

#### Plotly Documentation:  
- [parallel coordinates](https://plotly.com/python/parallel-coordinates-plot/) 

#### Contributed by:
This example app was contributed by [IcToxi](https://github.com/IcToxi)
"""

layout = example_app(filename, notes=notes)
