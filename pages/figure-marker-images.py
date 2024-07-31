import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app shows how to use images as markers in a Plotly figure",
)

filename = __name__.split("pages.")[1]

notes = """

#### Plotly Documentation:  
- [Scatter Plot](https://plotly.com/python/line-and-scatter/)
- [How to add images to charts as background images or logos](https://plotly.com/python/images/)

##### Contributed by:
This example app was contributed by [Mohamed Elauzei](https://community.plotly.com/u/mo.elauzei/summary)
for the [Figure Friday initiative](https://community.plotly.com/t/figure-friday-2024-week-29/85928/60)
"""

layout = example_app(filename, notes=notes)
