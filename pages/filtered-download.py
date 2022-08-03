import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This application allows you to filter a bar chart and download as HTML. It has a side-by-side layout and a regular-callback."
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [Dropdown](https://dash.plotly.com/dash-core-components/dropdown)
- [Download](https://dash.plotly.com/dash-core-components/download)

#### Plotly Documentation:  
- [Bar Plots](https://plotly.com/python/bar-charts/)

##### Contributed by:
This example app was contributed by [tolgahancepel](https://github.com/tolgahancepel)
"""

layout = example_app(filename, notes=notes)
