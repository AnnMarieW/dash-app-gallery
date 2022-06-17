import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Plotly Express scatter matrix example with top-down layout. This app contains adding components to graph via dropdown. ")

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:
- [Markdown](https://dash.plotly.com/dash-core-components/markdown)
- [Dropdown](https://plotly.com/python/dropdowns/)
- [Scatter Matrix](https://plotly.com/python/splom/)

#### Plotly Documentation:  
- [Plotly Express Overview](https://plotly.com/python/plotly-express/)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
