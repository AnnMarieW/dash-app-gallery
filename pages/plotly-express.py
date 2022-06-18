import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Plotly Express scatter matrix example with top-down layout. It has a top-bottom layout and a regular-callback. ")

filename = __name__.split("pages.")[1]


notes = """
#### Plotly Documentation:  
- [Plotly Express Overview](https://plotly.com/python/plotly-express/)

#### Dash Components in App:
- [Dropdown](https://plotly.com/python/dropdowns/)
- [Scatter Matrix](https://plotly.com/python/splom/)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
