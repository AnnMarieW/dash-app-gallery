import dash

from lib.code_and_show import example_app


dash.register_page(__name__, description="Analyze supply chain with a sankey diagram")

filename = __name__.split("pages.")[1]


notes = """

#### Plotly Documentation:  

- [Sankey Diagrams](https://plotly.com/python/sankey-diagram/)


#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
