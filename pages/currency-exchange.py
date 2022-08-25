import dash

from lib.code_and_show import example_app, make_app_first


dash.register_page(__name__, description="How to format numbers in a DataTable. This app uses top-down layout with regular-callback.")

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:  
- [DataTable](https://dash.plotly.com/datatable)
- See more information on [number formatting in the DataTable](https://dash.plotly.com/datatable/data-formatting)

#### Contributed by:
This example app was contributed by [AnnMariW](https://github.com/AnnMarieW)
"""

layout = example_app(filename, notes=notes, make_layout=make_app_first)
