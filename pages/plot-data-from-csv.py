import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="This application plots stocks data collected from csv. It contains button to invert axis on graph.")

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:
- [Button](https://dash.plotly.com/dash-core-components/markdown)
- [Graph](https://dash.plotly.com/dash-core-components/markdown)

#### Plotly Documentation:  
- [How plot data from csv file](https://plotly.com/python/plot-data-from-csv/)

##### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)
"""


layout = example_app(filename, notes=notes)
