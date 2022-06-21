import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app uses tabs to highlight cultural dimensions on a bar chart. It has a top-bottom layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]

# any notes will be displayed below the code-and-show page in a dcc.Markdown component
notes = """
#### Dash Components in App:
- [Dropdown](https://dash.plotly.com/dash-core-components/dropdown)

#### Plotly Documentation:
- [Bar Charts](https://plotly.com/python/bar-charts/)

#### Community Components:

Dash Bootstrap Components 
- [Layout](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/ "This component was made by the community and not officially maintained by Plotly.")
- [Card](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/ "This component was made by the community and not officially maintained by Plotly.")

##### Contributed by:
This example app was contributed by [tolgahancepel](https://github.com/tolgahancepel)
"""

layout = example_app(filename, notes=notes)
