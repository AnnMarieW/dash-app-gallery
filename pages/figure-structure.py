import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Accessing Plotly figure structures in Dash")

filename = __name__.split("pages.")[1]


notes = """
### For more information see:
Plotly docs:  

- [The structure of a figure - data, traces and layout explained.](https://plotly.com/python/figure-structure/)


### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""

layout = example_app(filename, notes=notes)
