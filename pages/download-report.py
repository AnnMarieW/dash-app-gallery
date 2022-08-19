import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="Application for text file reports. This app has a top-bottom layout and a regular callback."
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:
- [Button](https://dash.plotly.com/dash-html-components/button)
- [Markdown](https://dash.plotly.com/dash-core-components/markdown)
- [Download](https://dash.plotly.com/dash-core-components/download)

#### Plotly Documentation:  
- [Scatter Plot](https://plotly.com/python/line-and-scatter/)

#### Contributed by:
This example app was contributed by [Someshfengde](https://github.com/someshfengde)

"""


layout = example_app(filename, notes=notes)
