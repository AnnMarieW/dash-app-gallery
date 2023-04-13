import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app uses Gauge and Slider components to filter values for a scatter plot. It has a left-right layout with Dash Bootstrap Container component and has a regular-callback.",
)

filename = __name__.split("pages.")[1]


notes = """

#### Dash Components in the App:
- [Gauge](https://dash.plotly.com/dash-daq/gauge)
- [Slider](https://dash.plotly.com/dash-core-components/slider)

#### Plotly documentation:  
- [Scatter Plot](https://plotly.com/python/line-and-scatter/)

#### Community Components:

Dash Bootstrap Components
- [Themes](https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/)
- [Container](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/)

##### Contributed by:
This example app was contributed by [Jenna Le Noble](https://github.com/jennalenoble)

"""


layout = example_app(filename, notes=notes)
