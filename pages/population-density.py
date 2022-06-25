import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app shows Population Density Map by Year. It uses a top-down layout.",
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:

#### Plotly Documentation:   
- [choropleth](https://plotly.com/python/choropleth-maps/)

#### Community Components:

Dash Bootstrap Components 
- [Row and container](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/)

##### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)
"""

layout = example_app(filename)
