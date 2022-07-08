import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="Animated GDP and population over the years, using a RangeSlider, a bar plot and RadioItems. This app has a top-bottom layout and a regular-callback."
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:
- [RadioItems](https://dash.plotly.com/dash-core-components/radioitems)
- [Loading](https://dash.plotly.com/dash-core-components/loading)

#### Plotly Documentation:  
- [Intro to animations](https://plotly.com/python/animations/)
- [Bar Plot](https://plotly.com/python/bar-charts/)
- [Scatter Plot](https://plotly.com/python/line-and-scatter/)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
