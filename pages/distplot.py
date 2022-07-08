import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="Combined statistical representations; adding box, violin or rug subplot to a histogram. It has a top-bottom layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [RadioItems](https://dash.plotly.com/dash-core-components/radioitems)

#### Plotly Documentation:  
- [Distplots](https://plotly.com/python/distplot/)
- [Histograms](https://plotly.com/python/histograms/)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)
"""

layout = example_app(filename, notes=notes)
