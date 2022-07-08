import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="Stopwatch timer application with 1 button and an input field. This app uses top-down layout with regular-callback.",
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:
- [Input](https://dash.plotly.com/dash-core-components/input)
- [Interval](https://dash.plotly.com/dash-core-components/interval)
- [Power Button](https://dash.plotly.com/dash-daq/powerbutton)
- [LED Display](https://dash.plotly.com/dash-daq/leddisplay)

##### Contributed by:
This example app was contributed by [someshfengde](https://github.com/someshfengde)
"""


layout = example_app(filename, notes=notes)
