import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__, description="Interactive data-scaling using the secondary axis"
)

filename = __name__.split("pages.")[1]


notes = """

#### Plotly Documentation:  

- [Graph with multiple axes (dual y-axis plots, plots with secondary axes)](https://plotly.com/python/multiple-axes/)


#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
