import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app demonstrates pattern matching callbacks which dynamically adds or deletes components. It has a top-bottom layout and a pattern matching callback.",
)

filename = __name__.split("pages.")[1]

notes = """

#### Dash Components in App:
- [Dropdown](https://dash.plotly.com/dash-core-components/dropdown)
- [Callback Context](https://dash.plotly.com/determining-which-callback-input-changed)
- [Pattern Matching Callbacks](https://dash.plotly.com/pattern-matching-callbacks)
- [Medium Article Introducing Pattern Matching Callbacks](https://medium.com/plotly/pattern-matching-callbacks-in-dash-9014eee99858)

#### Plotly Components in App:
- [Line chart](https://plotly.com/python/line-charts/)
- [Scatter Plot](https://plotly.com/python/line-and-scatter/)

#### Community Components:

Dash Bootstrap Components 
- [Button component](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/button/ "This component was made by the community and not officially maintained by Plotly.")
- [Card component](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/ "This component was made by the community and not officially maintained by Plotly.")

##### Contributed by:
This example app was contributed by [AnnMarieW](https://github.com/AnnMarieW)

"""

layout = example_app(filename, notes=notes)
