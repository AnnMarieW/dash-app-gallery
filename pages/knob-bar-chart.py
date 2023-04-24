import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app uses Knob component to filter values in a bar chart. It has a side-by-side layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]


notes = """

#### Dash Components in the App:
- [Knob](https://dash.plotly.com/dash-daq/knob)

#### Plotly documentation:  
- [Bar Charts](https://plotly.com/python/bar-charts/)

#### Community Components:

Dash Bootstrap Components
- [Themes](https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/)
- [Layout](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/)

##### Contributed by:
This example app was contributed by [Jenna Le Noble](https://github.com/jennalenoble)

"""

layout = example_app(filename, notes=notes)
