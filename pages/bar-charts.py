import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="Bar Chart with a Dropdown",
)

filename = __name__.split("pages.")[1]


notes = """

#### Plotly Documentation:  

- [How to make Bar Charts](https://plotly.com/python/bar-charts/)


#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
