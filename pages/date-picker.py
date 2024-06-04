import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This application shows how to use the datepicker components",
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [DatePickerRange](https://dash.plotly.com/dash-core-components/datepickerrange)
- [DatePickerSingle](https://dash.plotly.com/dash-core-components/datepickersingle)


#### Plotly Documentation:
- [Line chart](https://plotly.com/python/line-charts/)

##### Contributed by:
This example app was contributed by [Nestor Solalinde](https://github.com/manolosolalinde)
"""

layout = example_app(filename, notes=notes)
