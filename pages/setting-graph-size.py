import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Adjusting graph width with Dash")

filename = __name__.split("pages.")[1]


notes = """
### For more information see:
Plotly docs:  

- [How to manipulate the graph size, margins and background color.](https://plotly.com/python/setting-graph-size/)


### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
