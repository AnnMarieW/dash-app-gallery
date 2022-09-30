import dash

from lib.code_and_show import example_app, make_app_first


dash.register_page(
    __name__,
    description="Interactive histogram where the mean, standard deviation sample size and number of bins is set with sliders and numeric inputs. It has a control panel in a sidebar in a responsive side-by-side layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [Slider](https://dash.plotly.com/dash-core-components/slider)

#### Plotly Documentation:  
- [Histograms](https://plotly.com/python/histograms/)

##### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)
"""

layout = example_app(filename, notes=notes, make_layout=make_app_first)
