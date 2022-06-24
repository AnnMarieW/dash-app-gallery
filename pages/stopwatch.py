import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="Stopwatch timer application with 1 button and an input field.",
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:
- [Input component](https://dash.plotly.com/dash-core-components/input)
- [Input component](https://dash.plotly.com/dash-core-components/interval)
- [Dash Daq components](https://dash.plotly.com/dash-daq)


##### Contributed by:
This example app was contributed by [someshfengde](https://github.com/someshfengde)
"""


layout = example_app(filename, notes=notes)
