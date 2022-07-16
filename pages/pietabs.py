import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This application shows how to use a datepicker with tabs and a pie chart. It has a side-by-side layout and regular-callbacks.",
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [DatePickerRange](https://dash.plotly.com/dash-core-components/datepickerrange)
- [Tabs](https://dash.plotly.com/dash-core-components/tabs)

#### Plotly Documentation:
- [Pie chart](https://plotly.com/python/pie-charts/)

##### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)
"""

layout = example_app(filename, notes=notes)
