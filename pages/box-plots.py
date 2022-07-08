import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="Interactive box plot with Checklist and RadioItems. It has a top-bottom layout and a regular-callback",
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:  
- [RadioItems](https://dash.plotly.com/dash-core-components/radioitems)
- [Checklist](https://dash.plotly.com/dash-core-components/checklist)

#### Plotly Documentation:  
- [Box Plots](https://plotly.com/python/box-plots/)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
