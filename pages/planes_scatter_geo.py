import dash

from lib.code_and_show import example_app

dash.register_page(
    __name__,
    description="This app shows connection between a dropdown and two graphs: scatter_geo and scatter_mapbox. It has a top-bottom layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]

notes = """

#### Dash Components in App:
- [Dropdown](https://dash.plotly.com/dash-core-components/dropdown)

#### Plotly Documentation:  
- [Scatter Mapbox](https://plotly.com/python/mapbox-layers/) 
- [Scatter Geo](https://plotly.com/python/bubble-maps/) 
- [Map Configuration: Mapbox Maps vs Geo Maps](https://plotly.com/python/map-configuration/)

#### Contributed by:
This example app was contributed by [someshfengde](https://github.com/someshfengde)

"""

layout = example_app(filename, notes=notes)
