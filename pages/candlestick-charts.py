import dash

from lib.code_and_show import example_app


dash.register_page(__name__, description="Candlestick chart with a range slider")

filename = __name__.split("pages.")[1]


notes = """

#### Plotly Documentation:  

- [Candlestick charts](https://plotly.com/python/candlestick-charts/)
How to make interactive candlestick charts in Python with Plotly. Six examples of candlestick charts with Pandas, time series, and yahoo finance data.

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
