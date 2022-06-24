import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__, description="Interactive network graph with Dash Cytoscape"
)

filename = __name__.split("pages.")[1]


notes = """

#### Dash Components in App:
- [Cytoscape](https://dash.plotly.com/cytoscape)

#### Plotly Documentation:  

- [How to make Network Graphs](https://plotly.com/python/network-graphs/)


#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
