import dash

from lib.code_and_show import example_app


dash.register_page(__name__, description="This app shows interactive pie chart with two dropdowns. It has a top-bottom layout and a regular-callback.")

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:
- [Dropdown](https://dash.plotly.com/dash-core-components/dropdown)

#### Plotly Documentation:  
- [Pie Chart](https://plotly.com/python/pie-charts/)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)
"""


layout = example_app(filename, notes=notes)
