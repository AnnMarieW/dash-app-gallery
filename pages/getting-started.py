import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__, description="This application shows the interaction between a Dropdown and a bar chart. It has a top-bottom layout and a regular-callback."
)

filename = __name__.split("pages.")[1]

notes = """

#### Dash Components in App:  
- [Dcc.Dropdown](https://dash.plotly.com/dash-core-components/dropdown)

#### Plotly Documentation:  
- [Bar Plots](https://plotly.com/python/bar-charts/)
- [Regular Callbacks](https://dash.plotly.com/basic-callbacks)


#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
