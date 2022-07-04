import dash

from lib.code_and_show import example_app


dash.register_page(__name__, description="Changing the position of data points")

filename = __name__.split("pages.")[1]


notes = """

#### Plotly Documentation:  

- [How to make SVG shapes. Examples of lines, circle, rectangle, and path.](https://plotly.com/python/shapes/)


#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
