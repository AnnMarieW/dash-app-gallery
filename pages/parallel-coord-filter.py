import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app uses a parallel coordinates graph and the selected coordinates to filter a Dash AG Grid. It has a top-bottom layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]

notes = """

#### Dash Components in App:
- [Dash AG Grid](https://dash.plotly.com/dash-ag-grid)
- [Store](https://dash.plotly.com/dash-core-components/store)

#### Plotly Documentation:  
- [parallel coordinates](https://plotly.com/python/parallel-coordinates-plot/) 

#### Community Components:

Dash Bootstrap Components
- [Themes](https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/)
- [Container](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/)

#### Contributed by:
This example app was contributed by [Bryan](https://community.plotly.com/u/jinnyzor/summary),
Please see more information about this topic on the [Dash Community Forum](https://community.plotly.com/t/filtering-a-datatable-with-parallel-coordinates/74338)

"""

layout = example_app(filename, notes=notes)
