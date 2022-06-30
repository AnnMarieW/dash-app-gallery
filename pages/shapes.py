import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="This app changes the figure accoring to data points.This app uses top-down layout with regular callback.")

filename = __name__.split("pages.")[1]


notes = """
#### Dash components in App: 
- [Scatter](https://plotly.com/python/line-and-scatter/)

#### Plotly Documentation:  
- [How to make SVG shapes. Examples of lines, circle, rectangle, and path.](https://plotly.com/python/shapes/)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)
"""


layout = example_app(filename, notes=notes)
