import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Updating the figure layout using a Slider, and an Input. This app has a top-bottom layout and a regular-callback.")

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:  
- [Dcc.Input](https://dash.plotly.com/dash-core-components/input)
- [Dcc.Slider](https://dash.plotly.com/dash-core-components/slider)

#### Plotly Documentation:  
- [Sliders](https://plotly.com/python/sliders/)
- [Creating and updating figures](https://plotly.com/python/creating-and-updating-figures)


#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
