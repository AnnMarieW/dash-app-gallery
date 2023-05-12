import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app uses Graduated Bar and Slider components to filter a bar chart. It has a side-by-side layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in the App:
- [Graduated Bar](https://dash.plotly.com/dash-daq/graduatedbar)
- [Slider](https://dash.plotly.com/dash-daq/slider)

#### Plotly documentation:  
- [Bar Charts](https://plotly.com/python/bar-charts/)

#### Community Components:

Dash Bootstrap Components
- [Layout](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/)

##### Contributed by:
This example app was contributed by [Jenna Le Noble](https://github.com/jennalenoble)

"""


layout = example_app(filename, notes=notes)
