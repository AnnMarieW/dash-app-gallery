import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app uses the Boolean Switch component to turn a graph on and off. It has a top-bottom layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in the App:
- [Boolean Switch](https://dash.plotly.com/dash-daq/booleanswitch)

#### Plotly documentation:  
- [Line Chart](https://plotly.com/python/line-charts/)


##### Contributed by:
This example app was contributed by [Jenna Le Noble](https://github.com/jennalenoble)

"""


layout = example_app(filename, notes=notes)
