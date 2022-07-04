import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="How to save interactive HTML versions of your figures to your local disk. It has a top-bottom layout.",
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [Button](https://dash.plotly.com/dash-html-components/button)

#### Plotly Documentation:  
- [Scatter Plot](https://plotly.com/python/line-and-scatter/)
- [Interactive HTML Export](https://plotly.com/python/interactive-html-export/)

##### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)
"""

layout = example_app(filename, notes=notes)
