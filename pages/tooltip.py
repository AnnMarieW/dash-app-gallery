import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__, description="This app uses a tooltip to display breakdown of profit per month and segment. It uses a simple layout and regular-callback."
)

filename = __name__.split("pages.")[1]


notes = """

#### Dash Components in the App:
- [Tooltip](https://dash.plotly.com/dash-core-components/tooltip)

#### Plotly documentation:  
- [Bar Chart](https://plotly.com/python/bar-charts/)

##### Contributed by:
This example app was contributed by [Milan Mitrovic](https://milanzmitrovic.github.io)

"""


layout = example_app(filename, notes=notes)
