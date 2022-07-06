import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="This app demonstrate the use of subplots with adjustable width. This app uses top-down layout with regular callback.")

filename = __name__.split("pages.")[1]


notes = """
#### Dash components in App: 
- [Slider](https://dash.plotly.com/dash-core-components/slider)

#### Plotly Documentation:  
- [Subplots](https://plotly.com/python/subplots/)
How to make subplots in with Plotly's Python graphing library. Examples of stacked, custom-sized, gridded, and annotated subplots.

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
