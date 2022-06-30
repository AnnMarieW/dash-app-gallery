import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="Demonstrate use of Sunburst chart with continuous color adjustable via dropdown. This app uses top-down layout with regular callback.",
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:
- [Dropdown](https://dash.plotly.com/dash-core-components/dropdown)

#### Plotly Documentation:  
- [Sunburst plots](https://plotly.com/python/sunburst-charts/)

#### Community Components:
Dash Bootstrap Components 
- [Col,Container and Row](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
