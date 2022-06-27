import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="Interactive Plotly Axes Labels example in a bar plot. This app has a top-bottom layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]


notes = """

#### Dash Components in App:  
- [Dcc.Dropdown](https://dash.plotly.com/dash-core-components/dropdown)

#### Plotly Documentation:  
- [Adjusting the axes properties](https://plotly.com/python/axes/)
- [Bar Plot](https://plotly.com/python/bar-charts/)

Learn how to adjust axes properties in Python - axes titles, styling and coloring axes and grid lines, ticks, tick labels and more.

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
