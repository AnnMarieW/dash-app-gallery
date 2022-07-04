import dash

from lib.code_and_show import example_app


dash.register_page(__name__, description="This app shows how to interactively change the marker borders. It has a top-bottom layout and a regular-callback.")

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:
- [Daq Color Picker](https://dash.plotly.com/dash-daq/colorpicker)

#### Plotly Documentation:  
- [How to style markers]](https://plotly.com/python/marker-style/)
- [Scatter Plots] (https://plotly.com/python/line-and-scatter/)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)
"""


layout = example_app(filename, notes=notes)
