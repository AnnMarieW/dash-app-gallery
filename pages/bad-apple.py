import dash
from dash import html, dcc

from utils.code_and_show import example_app, make_app_first


dash.register_page(
    __name__,
    description="An app that uses clientside callback to display frames because dcc Interval is activated multiple times per second.",
    layout_type="top-bottom",
    components_type=["store", "interval"],
    graph_type=None,
    callback_type="clientside",
)

filename = __name__.split("pages.")[1]

# any notes will be displayed below the code-and-show page in a dcc.Markdown component
notes = """
### For more information see:
Dash docs:  

- [Interval component](https://dash.plotly.com/dash-core-components/interval)

- [Store component](https://dash.plotly.com/dash-core-components/store)

- [Clientside Callback](https://dash.plotly.com/clientside-callbacks)


### Contributed by:
This example app was contributed by [IcToxi](https://github.com/IcToxi)

"""

layout = html.Div(
    [
        example_app(filename, make_layout=make_app_first),
        dcc.Markdown(notes, className="m-4"),
    ]
)
