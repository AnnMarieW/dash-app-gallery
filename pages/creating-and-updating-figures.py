import dash

from lib.code_and_show import example_app


dash.register_page(__name__, description="Updating the figure layout")

filename = __name__.split("pages.")[1]


notes = """

#### Plotly Documentation:  

- [Creating and updating figures](https://plotly.com/python/creating-and-updating-figures)


#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
