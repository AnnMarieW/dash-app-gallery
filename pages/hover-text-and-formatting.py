import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Demo of the hover modes")

filename = __name__.split("pages.")[1]


notes = """

#### Plotly Documentation:  

- [How to use hover text and formatting ](https://plotly.com/python/hover-text-and-formatting/)


#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""

layout = example_app(filename, notes=notes)
