import dash

from lib.code_and_show import example_app

dash.register_page(
    __name__,
    description="This app connects between two Input components and a scatter geo. It has a top-down layout with a circular-callback and callback context.",
)

filename = __name__.split("pages.")[1]

notes = """

#### Dash Components in App:
- [Input](https://dash.plotly.com/dash-core-components/input)

#### Plotly Components in App:
- [Scatter Geo](https://plotly.com/python/bubble-maps/)

##### Contributed by:
This example app was contributed by [Pierre-Olivier](https://github.com/pierreolivierbonin)

"""

layout = example_app(filename, notes=notes)
