import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__, description="Interactive Mapbox Choropleth Map of Montreal. This app has a top-bottom layout and a regular-callback."
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:  
- [RadioItems](https://dash.plotly.com/dash-core-components/radioitems)

#### Plotly Documentation:  
- [Choropleth maps](https://plotly.com/python/choropleth-maps/)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
