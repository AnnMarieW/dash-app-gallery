import dash

from lib.code_and_show import example_app


dash.register_page(__name__, description="This app connects between RadioItems and a graph to change the text position of annotations. It has a top-bottom layout with a regular-callback.")

filename = __name__.split("pages.")[1]


notes = """

#### Dash Components in the App:
- [RadioItems](https://dash.plotly.com/dash-core-components/radioitems)

#### Plotly documentation:  
- [How to add text labels and annotations to plots](https://plotly.com/python/text-and-annotations/)
- [Scatter Plot](https://plotly.com/python/line-and-scatter/)

##### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
