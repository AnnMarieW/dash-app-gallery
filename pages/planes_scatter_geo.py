import dash
from dash import html, dcc

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app connects between a dropdown and two graphs: scatter_geo (also called Bubble map) and scatter_mapbox",
    layout_type="top-bottom",
    components_type=["dropdown"],
    graph_type="ScatterGeo and Scatter Mapbox",
    callback_type="general",
)

filename = __name__.split("pages.")[1]

# any notes will be displayed below the code-and-show page in a dcc.Markdown component
notes = """
### For more information see:
Dash docs:  

- [Dropdown component](https://dash.plotly.com/dash-core-components/dropdown)

Plotly docs:  

- [Scatter Mapbox](https://plotly.com/python/mapbox-layers/) 
- [Scatter Geo](https://plotly.com/python/bubble-maps/) 

### Contributed by:
This example app was contributed by [someshfengde](https://github.com/someshfengde)

"""

layout = html.Div([example_app(filename), dcc.Markdown(notes, className="m-4")])
