import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app let's the user download datatable data as excel or csv files, using the dcc.Download component and a dropdown. It has a top-bottom layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [DataTable](https://dash.plotly.com/datatable)
- [Dropdown](https://dash.plotly.com/dash-core-components/dropdown)
- [Download](https://dash.plotly.com/dash-core-components/download)

#### Community Components:

Dash Bootstrap Components
- [Button](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/button/ "This component was made by the community and not officially maintained by Plotly.")

##### Contributed by:
- This app was built by [Milan](https://milanzmitrovic.github.io/)

"""

layout = example_app(filename, notes=notes)
