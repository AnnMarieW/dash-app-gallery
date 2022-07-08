import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="Demo of the hover modes. It has a top-bottom layout and a regular-callback."
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [RadioItems](https://dash.plotly.com/dash-core-components/radioitems)

#### Plotly Documentation:  
- [Line Plot](https://plotly.com/python/line-charts/)
- [Hover Text and Formatting](https://plotly.com/python/hover-text-and-formatting/)

##### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)
"""

layout = example_app(filename, notes=notes)
