import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="Discrete and continuous color scales. It has a top-bottom layout and a regular-callback."
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [RadioItems](https://dash.plotly.com/dash-core-components/radioitems)

#### Plotly Documentation:
- [Scatter Plot](https://plotly.com/python/line-and-scatter/)
- [Discrete vs Continuous Color](https://plotly.com/python/discrete-color/)

##### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)
"""

layout = example_app(filename, notes=notes)
