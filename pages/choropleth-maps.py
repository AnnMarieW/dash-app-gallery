import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__, description="Interactive Mapbox Choropleth Map of US Counties"
)

filename = __name__.split("pages.")[1]


notes = """

#### Plotly Documentation:  

- [Choropleth maps](https://plotly.com/python/mapbox-county-choropleth/)
How to make an interactive Mapbox Choropleth Map of US Counties.

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
