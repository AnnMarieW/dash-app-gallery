import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Subplots with adjustable width")

filename = __name__.split("pages.")[1]


notes = """
### For more information see:
Plotly docs:  

- [Subplots](https://plotly.com/python/subplots/)
How to make subplots in with Plotly's Python graphing library. Examples of stacked, custom-sized, gridded, and annotated subplots.


### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
