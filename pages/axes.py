import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="Interactive Plotly Axes Labels",
    callback_dd="1 Output 1 Input",
)

filename = __name__.split("pages.")[1]


notes = """
### For more information see:
Plotly docs:  

- [Adjusting the axes properties](https://plotly.com/python/axes/)

Learn how to adjust axes properties in Python - axes titles, styling and coloring axes and grid lines, ticks, tick labels and more.


### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
