import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__, description="This app does an Analysis of the ML model's results using ROC and PR curves. This app uses top-down layout with a regular callback."
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:
- [Dropdown](https://dash.plotly.com/dash-core-components/dropdown)

#### Plotly Documentation:  
- [ROC and PR Curves](https://plotly.com/python/roc-and-pr-curves/)
- [Adding Lines to Figures](https://plotly.com/python/shapes/)
- [Area](https://plotly.com/python/filled-area-plots/)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
