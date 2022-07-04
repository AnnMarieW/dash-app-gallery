import dash

from lib.code_and_show import example_app


dash.register_page(__name__, description="Set the color scale with a Dropdown")

filename = __name__.split("pages.")[1]


notes = """

#### Plotly Documentation:  

- [Continuous Color Scales and Color Bars](https://plotly.com/python/colorscales/)
How to set, create and control continuous color scales and color bars in scatter, bar, map and heatmap figures.

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
