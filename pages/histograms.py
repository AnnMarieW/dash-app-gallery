import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="Interactive histogram where the Slider sets the mean and standard deviation. It has a top-bottom layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [Slider](https://dash.plotly.com/dash-core-components/slider)

#### Plotly Documentation:  
- [Histograms](https://plotly.com/python/histograms/)

##### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)
"""

layout = example_app(filename, notes=notes)
