import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Interactive pie chart with two dropdowns")

filename = __name__.split("pages.")[1]


notes = """
### For more information see:
Plotly docs:  

- [How to make a pie chart](https://plotly.com/python/pie-charts/)


### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
