import dash

from lib.code_and_show import example_app

description = """
This app shows how to add a custom Vis.js Timeline component. It uses `set_props` to update a `dcc.Store` component
 when clicking on a timeline item. This allows you to interact with a custom component  using Dash callbacks.
"""

dash.register_page(__name__, description=description)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Documentation: 
- [Clientside Callbacks ](https://dash.plotly.com/clientside-callbacks#set-props)

#### Contributed by:
This example app was contributed by [AnnMarieW](https://github.com/AnnMarieW)
"""


layout = example_app(filename, notes=notes)
