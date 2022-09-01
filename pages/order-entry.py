import dash

from lib.code_and_show import example_app


dash.register_page(__name__, description="This app demonstrates adding and deleting rows, formatting numbers and dropdowns in the DataTable."
                                         "  It uses top-down layout with regular-callback and uses callback context to determine which input triggerd the callback.")

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:  
- [DataTable](https://community.plotly.com/u/annmariew/summary)
- [Button](https://dash.plotly.com/dash-html-components/button)
- [Callback Context](https://dash.plotly.com/advanced-callbacks#determining-which-input-has-fired-with-dash.callback_context)

#### Contributed by:
This example app was contributed by [AnnMarieW](https://plotly.com/python/)
"""

layout = example_app(filename, notes=notes)
