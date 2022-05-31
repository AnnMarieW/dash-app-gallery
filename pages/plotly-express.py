import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Plotly Express scatter matrix")

filename = __name__.split("pages.")[1]


notes = """

#### Plotly Documentation:  

- [Plotly Express Overview](https://plotly.com/python/plotly-express/)


#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
