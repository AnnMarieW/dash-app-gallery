import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="DataTable with callback on cell click")

filename = __name__.split("pages.")[1]

notes = """

Dash docs:  

- [DataTable component](https://dash.plotly.com/datatable)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""

layout = example_app(filename, notes=notes)
