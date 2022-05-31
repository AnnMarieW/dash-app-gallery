import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Scatter chart")

filename = __name__.split("pages.")[1]


notes = """

#### Plotly Documentation:  

- [Line and Scatter Chart](https://plotly.com/python/line-and-scatter/)
How to make interactive line and scatter charts 

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
