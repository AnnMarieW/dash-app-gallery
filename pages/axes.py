import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="Interactive Plotly Axes Labels example in a bar plot. This app has a top-bottom layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]


notes = """

#### Dash Components in App:  
- [Button](https://dash.plotly.com/dash-html-components/button)

#### Plotly Documentation:  
- [Adjusting the axes properties](https://plotly.com/python/axes/)
- [Histogram](https://plotly.com/python/histograms)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
