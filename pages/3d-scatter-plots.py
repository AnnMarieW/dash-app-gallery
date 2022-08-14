import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__, description="Iris samples in a scatter_3d plot filtered by petal width with a RangeSlider. This app has a top-bottom layout and a regular-callback."
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in the App:
- [Range Slider](https://dash.plotly.com/dash-core-components/rangeslider)

#### Plotly documentation:  
- [3d Scatter Plots](https://plotly.com/python/3d-scatter-plots/)


##### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""



layout = example_app(filename, notes=notes)
