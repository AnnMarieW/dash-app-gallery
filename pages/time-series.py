import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__, description="This app uses a dropdown to display stock prices on a line chart by Stock name. It uses a top-bottom layout and a regular-callback."
)

filename = __name__.split("pages.")[1]


notes = """

#### Dash Components in the App:
- [Dropdown](https://dash.plotly.com/dash-core-components/dropdown)

#### Plotly documentation:  
- [How plot time series data](https://plotly.com/python/time-series/)
- [Line Chart](https://plotly.com/python/line-charts/)

##### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
