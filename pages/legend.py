import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Interactively change the legend position")

filename = __name__.split("pages.")[1]


notes = """

#### Plotly Documentation:  

- [How to configure and style the legend](https://plotly.com/python/legend/)


#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""

layout = example_app(filename, notes=notes)
