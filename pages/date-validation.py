import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This application shows the connections between a Datepicker and an Alert. It has a top-bottom layout and regular-callback.",
)

filename = __name__.split("pages.")[1]

# any notes will be displayed below the code-and-show page in a dcc.Markdown component
notes = """
#### Dash Components in App:
- [Markdown](https://dash.plotly.com/dash-core-components/markdown)

#### Community Components:

Dash Bootstrap Components 
- [Button](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/button/ "This component was made by the community and not officially maintained by Plotly.")
- [Alert](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/alert/ "This component was made by the community and not officially maintained by Plotly.")

Dash Mantine Components
- [DatePicker](https://www.dash-mantine-components.com/components/datepicker "This component was made by the community and not officially maintained by Plotly.")

##### Contributed by:
This example app was contributed by [someshfengde](https://github.com/someshfengde)
"""

layout = example_app(filename, notes=notes)
