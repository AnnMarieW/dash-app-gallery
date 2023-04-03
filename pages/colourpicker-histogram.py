import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app shows a histogram of life expectancy and uses ColourPicker to change the colour of the bars. This app has a top-bottom layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:
- [Loading](https://dash.plotly.com/dash-core-components/loading)
- [ColorPicker](https://dash.plotly.com/dash-daq/colorpicker)


#### Plotly Documentation:  
- [Histogram](https://plotly.com/python/histograms/)
- [Themes](https://plotly.com/python/templates/)

#### Contributed by:
This example app was contributed by [Jenna Le Noble](https://github.com/jennalenoble)
"""

layout = example_app(filename, notes=notes)
