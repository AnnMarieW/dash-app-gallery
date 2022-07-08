import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This application plots line on a map between the selected countries. It has a top-bottom layout and a chained callback.",
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [Dropdown](https://dash.plotly.com/dash-core-components/dropdown)
- [Chained Callback](https://dash.plotly.com/basic-callbacks#dash-app-with-chained-callbacks)

#### Plotly Documentation:
- [Lines on Maps](https://plotly.com/python/lines-on-maps/)

##### Contributed by:
This example app was contributed by [tolgahancepel](https://github.com/tolgahancepel)
"""

layout = example_app(filename, notes=notes)
