import dash

from lib.code_and_show import example_app, make_app_first

dash.register_page(
    __name__,
    description="This app connects between the dropdown and the graphs to update the figure templates for each graph. It has a top-down layout with a regular-callback.",
)

filename = __name__.split("pages.")[1]

notes = """

#### Dash Components in App:
- [Dropdown](https://dash.plotly.com/dash-core-components/dropdown)

#### Plotly Components in App:
- [Scatter Mapbox](https://plotly.com/python/mapbox-layers/)
- [Violin Plot](https://plotly.com/python/violin/)
- [Scatter Plot](https://plotly.com/python/line-and-scatter/)

##### Contributed by:
This example app was contributed by [Tuomas](https://github.com/tuopouk)

"""

layout = example_app(filename, notes=notes, make_layout=make_app_first)
