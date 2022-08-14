import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="Select the color of the title and figure labels with a colorpicker. It has a top-bottom layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [Color Picker](https://dash.plotly.com/dash-daq/colorpicker)

#### Plotly Documentation:  
- [Scatter Plot](https://plotly.com/python/line-and-scatter/)
- [Setting the Font, Title, Legend Entries, and Axis Titles](https://plotly.com/python/figure-labels/)

##### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)
"""

layout = example_app(filename, notes=notes)
