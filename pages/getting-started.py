import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__, description="Getting started with Dash and Plotly", order=0
)

filename = __name__.split("pages.")[1]

notes = """
### For more information see:
Plotly docs:  

- [Getting Started with Dash and Plotly](https://plotly.com/python/getting-started/)

Dash docs:

- [Dash Tutorial](https://dash.plotly.com/installation)


### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
