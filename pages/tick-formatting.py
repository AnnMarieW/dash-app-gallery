import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Linear Tick Formatting")

filename = __name__.split("pages.")[1]


notes = """
### For more information see:
Plotly docs:  

- [How to format axes ticks ](https://plotly.com/python/tick-formatting/)


### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
