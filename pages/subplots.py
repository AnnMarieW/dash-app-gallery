import dash

from lib.code_and_show import example_app


dash.register_page(__name__, description="This app demonstrate the use of subplots with adjustable width. This app uses top-down layout with regular-callback.")

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App: 
- [Slider](https://dash.plotly.com/dash-core-components/slider)

#### Plotly Documentation:  
- [Subplots](https://plotly.com/python/subplots/)
- [Scatter Plot](https://plotly.com/python/line-and-scatter/)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
