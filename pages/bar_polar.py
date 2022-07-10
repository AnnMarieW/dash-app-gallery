import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__, description="This app connects between the dropdown, the radio button, and the bar polar chart. It has a top-bottom layout and a regular-callback."
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in the App:
- [RadioItems](https://dash.plotly.com/dash-core-components/radioitems)
- [Dropdown](https://dash.plotly.com/dash-core-components/dropdown)

#### Plotly documentation:  
- [Polar Bar Charts](https://plotly.com/python/wind-rose-charts/)

##### Contributed by:
This example app was contributed by [Pierre-Olivier](https://github.com/pierreolivierbonin)

"""


layout = example_app(filename, notes=notes)