import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="Accessing Plotly figure structures in Dash. It has a top-bottom layout and a regular-callback."
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [Clipboard](https://dash.plotly.com/dash-core-components/clipboard)

#### Plotly Documentation:
- [The structure of a figure - data, traces and layout explained.](https://plotly.com/python/figure-structure/)

##### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)
"""

layout = example_app(filename, notes=notes)