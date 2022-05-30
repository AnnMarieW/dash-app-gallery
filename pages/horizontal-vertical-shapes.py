import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__, description="Iris plot with an interactive horizontal line"
)

filename = __name__.split("pages.")[1]


notes = """
### For more information see:
Plotly docs:  

- [How to add annotated horizontal and vertical lines](https://plotly.com/python/horizontal-vertical-shapes/)


### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""

layout = example_app(filename, notes=notes)
