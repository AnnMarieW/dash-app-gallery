import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app let's the user download datatable data as excel or csv files, using the dcc.Download component and a dropdown.",
    layout_type="top-bottom",
    components_type=["button", "dropdown", "datatable", "download"],
    graph_type="datatable",
    callback_type="general",
)

filename = __name__.split("pages.")[1]

# any notes will be displayed below the code-and-show page in a dcc.Markdown component
notes = """
#### Dash Components in App:
- [DataTable component](https://dash.plotly.com/datatable)
- [Dropdown component](https://dash.plotly.com/dash-core-components/dropdown)
- [Download component](https://dash.plotly.com/dash-core-components/download)

#### 3rd-party Dash Bootstrap Components: 
- [Button component](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/button/ "This component was made by the community and not officially maintained by Plotly.")

##### Contributed by:
- This app was built by [Milan](https://milanzmitrovic.github.io/)

"""

layout = example_app(filename, notes=notes)
