import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="Application for downloading the graph plots. This app has a top-bottom layout and a regular-callback."
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:
- [Dropdown](https://dash.plotly.com/dash-core-components/dropdown)
- [Download](https://dash.plotly.com/dash-core-components/download)

#### Plotly Documentation:  
- [Scatter Plot](https://plotly.com/python/line-and-scatter/)

#### Contributed by:
This example app was contributed by [Someshfengde](https://github.com/someshfengde)

"""


layout = example_app(filename, notes=notes)
