import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="This application plots stocks data collected from csv. It has a top-bottom layout and a regular-callback.")

filename = __name__.split("pages.")[1]


notes = """
#### Plotly Documentation:  
- [How plot data from csv file](https://plotly.com/python/plot-data-from-csv/)

#### Dash Components in App:
- [Button](https://dash.plotly.com/dash-html-components/button)
- [Line](https://plotly.com/python/line-charts/)

##### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)
"""


layout = example_app(filename, notes=notes)
