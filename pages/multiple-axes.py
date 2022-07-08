import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__, description="This app shows interactive data-scaling using the secondary axis. It has a top-bottom layout and a regular-callback."
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:
- [Radio Items](https://dash.plotly.com/dash-core-components/radioitems)

#### Plotly Documentation:  
- [Graph with multiple axes (dual y-axis plots, plots with secondary axes)](https://plotly.com/python/multiple-axes/)
- [Scatter Plot](https://plotly.com/python/line-and-scatter/)
- [Plotly Subplots](https://plotly.com/python/subplots/)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)
"""


layout = example_app(filename, notes=notes)
