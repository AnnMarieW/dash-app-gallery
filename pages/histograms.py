import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="Interactive histogram. Set the mean and standard deviation with a Slider",
)

filename = __name__.split("pages.")[1]


notes = """

#### Plotly Documentation:  

- [Histograms](https://plotly.com/python/histograms/)


#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""

layout = example_app(filename, notes=notes)
