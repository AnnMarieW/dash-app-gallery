import dash
from lib.code_and_show import example_app

dash.register_page(
    __name__,
    description="Two tabs that plot the Iris and Gapminder data on a bubble chart and scatter graph. ",
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [Tabs](https://dash.plotly.com/dash-core-components/tabs)

#### Plotly Documentation:  
- [Scatter plots](https://plotly.com/python/line-and-scatter/)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""

layout = example_app(filename, notes=notes)
