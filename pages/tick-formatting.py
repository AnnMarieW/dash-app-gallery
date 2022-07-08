import dash

from lib.code_and_show import example_app


dash.register_page(__name__, description="This app uses the checklist to allow for linear ticks in the scatter plot. It has a top-bottom layout and a regular-callback.")

filename = __name__.split("pages.")[1]


notes = """

#### Dash Components in the App:
- [Checklist](https://dash.plotly.com/dash-core-components/checklist)

#### Plotly documentation:  
- [How to format axes ticks ](https://plotly.com/python/tick-formatting/)
- [Scatter Plot](https://plotly.com/python/line-and-scatter/)

##### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
