import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app demonstrates pattern matching callbacks which dynamically adds or deletes components",
    layout_type="top-bottom",
    graph_type="scatter",
    callback_type="pattern-matching",
)

filename = __name__.split("pages.")[1]

# any notes will be displayed below the code-and-show page in a dcc.Markdown component
notes = """
### For more information see:

- [Medium Article Introducing Pattern Matching Callbacks](https://medium.com/plotly/pattern-matching-callbacks-in-dash-9014eee99858)

Dash docs:  

- [Pattern Matching Callbacks](https://dash.plotly.com/pattern-matching-callbacks)

Plotly docs:  

- [parallel coordinates](https://plotly.com/python/parallel-coordinates-plot/) 

### Contributed by:
This example app was contributed by [AnnMarieW](https://github.com/AnnMarieW)

"""

layout = example_app(filename, notes=notes)
