import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Candlestick chart with a range slider. This app has a top-bottom layout and a regular-callback.")

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:  
- [Checklist](https://dash.plotly.com/dash-core-components/checklist)

#### Plotly Documentation:  

- [Candlestick charts](https://plotly.com/python/candlestick-charts/)
- [RangeSlider](https://plotly.com/python/range-slider/)
How to make interactive candlestick charts in Python with Plotly. Six examples of candlestick charts with Pandas, time series, and yahoo finance data.

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
