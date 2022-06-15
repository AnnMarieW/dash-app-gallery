import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app demonstrates pattern matching callbacks which dynamically adds or deletes components",
)

filename = __name__.split("pages.")[1]

# any notes will be displayed below the code-and-show page in a dcc.Markdown component
notes = """
### For more information see:

- [Medium Article Introducing Pattern Matching Callbacks](https://medium.com/plotly/pattern-matching-callbacks-in-dash-9014eee99858)

#### Dash Components in App:
- [Pattern Matching Callbacks](https://dash.plotly.com/pattern-matching-callbacks)
- [Callback Context](https://dash.plotly.com/determining-which-callback-input-changed)
- [Dropdown component](https://dash.plotly.com/dash-core-components/dropdown)

#### Plotly Components in App:
- [Line chart](https://plotly.com/python/line-charts/)

#### Community Components:

Dash Bootstrap Components 
- [Button component](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/button/ "This component was made by the community and not officially maintained by Plotly.")
- [Card component](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/ "This component was made by the community and not officially maintained by Plotly.")

##### Contributed by:
This example app was contributed by [AnnMarieW](https://github.com/AnnMarieW)

"""

layout = example_app(filename, notes=notes)
