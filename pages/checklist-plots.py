import dash
from lib.code_and_show import example_app

dash.register_page(
    __name__,
    description="An app that plots the Iris data set combined with the checklist. This app has a top-bottom layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:
- [Checklist](https://dash.plotly.com/dash-core-components/checklist)

#### Plotly Documentation:  
- [Scatter Plot](https://plotly.com/python/line-and-scatter/)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
