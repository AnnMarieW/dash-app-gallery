import dash

from utils.code_and_show import example_app



dash.register_page(
    __name__,
    description="This app shows Population Density Map by Year. It uses a top-down layout.",
)

filename = __name__.split("pages.")[1]

notes = """
#### Plotly Documentation:   
- [choropleth](https://plotly.com/python/choropleth-maps/)

##### Contributed by:
This example app was contributed by [Tolga](https://github.com/tolgahancepel)
"""

layout = example_app(filename, notes=notes)
