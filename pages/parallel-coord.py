import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app connects between selected rows in a Dash DataTable to update traces of a parallel coordinates graph.",
)

filename = __name__.split("pages.")[1]

# any notes will be displayed below the code-and-show page in a dcc.Markdown component
notes = """

Dash docs:  

- [DataTable component](https://dash.plotly.com/datatable)

#### Plotly Documentation:  

- [parallel coordinates](https://plotly.com/python/parallel-coordinates-plot/) 

#### Contributed by:
This example app was contributed by [IcToxi](https://github.com/IcToxi)

"""

layout = example_app(filename, notes=notes)
