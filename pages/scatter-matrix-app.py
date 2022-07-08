import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This application shows the connections between a Multi Dropdown and a Scatterplot Matrix graph. It has a top-bottom layout and regular-callback.",
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [Dropdown](https://dash.plotly.com/dash-core-components/dropdown)

#### Plotly Documentation:
- [Scatterplot Matrix](https://plotly.com/python/splom/)

##### Contributed by:
This example app was contributed by [Pierre-Olivier](https://github.com/pierreolivierbonin)
"""

layout = example_app(filename, notes=notes)
