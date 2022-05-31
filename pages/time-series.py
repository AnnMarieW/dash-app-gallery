import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__, description="Stock price analysis - plotting time series data"
)

filename = __name__.split("pages.")[1]


notes = """
### For more information see:
Plotly docs:  

- [How plot time series data](https://plotly.com/python/time-series/)


### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
