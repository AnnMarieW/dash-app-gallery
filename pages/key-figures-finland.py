import dash

from lib.code_and_show import example_app, make_app_first

dash.register_page(
    __name__,
    description="This app displays data from Statistics Findand. It has a side-by-side layout with a clientside-callback.",
)

filename = __name__.split("pages.")[1]

notes = """

#### Dash Components in App:
- [Dropdown](https://dash.plotly.com/dash-core-components/dropdown)
- [Store](https://dash.plotly.com/dash-core-components/store)
- [Clientside Callback](https://dash.plotly.com/clientside-callbacks)

#### Plotly Components in App:
- [Mapbox Choropleth Maps](https://plotly.com/python/mapbox-county-choropleth/)


##### Contributed by:
This example app was contributed by [Tuomas](https://github.com/tuopouk).  See the fully-featured app [here](https://keyfiguresfinland.herokuapp.com/)

"""

layout = example_app(filename, notes=notes, make_layout=make_app_first)
