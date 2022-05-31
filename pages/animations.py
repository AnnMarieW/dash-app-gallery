import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="Animated GDP and population over decades",
    callback_dd="1 Output 1 Input",
)

filename = __name__.split("pages.")[1]


notes = """
### For more information see:
Plotly docs:  

- [Intro to animations](https://plotly.com/python/animations/)


### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
