import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app uses Clipboard component to be able to copy the mtcars dataset as a csv. It includes an interactive scatter plot that uses RadioItems to be able to select the x variable. This app has a top-bottom layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:
- [Clipboard](https://dash.plotly.com/dash-core-components/clipboard)
- [DataTable](https://dash.plotly.com/datatable)
- [RadioItems](https://dash.plotly.com/dash-core-components/radioitems)

#### Plotly Documentation:  
- [Scatter Plots](https://plotly.com/python/line-and-scatter/)

#### Contributed by:
This example app was contributed by [Jenna Le Noble](https://github.com/jennalenoble)
"""


layout = example_app(filename, notes=notes)
