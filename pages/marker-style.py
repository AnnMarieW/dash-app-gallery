import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Interactively change the marker borders.")

filename = __name__.split("pages.")[1]


notes = """

#### Plotly Documentation:  

- [How to style markers](https://plotly.com/python/marker-style/)
How to make interactive line and scatter charts 

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
