import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="Sunburst chart with continuous color scale.  Select gapminder data by year with a Dropdown component",
    layout_type="side by side",
    components_type=["dropdown"],
    graph_type="sunburst",
)

filename = __name__.split("pages.")[1]



notes = """

#### Plotly Documentation:  

- [Sunburst plots](https://plotly.com/python/sunburst-charts/)


#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
