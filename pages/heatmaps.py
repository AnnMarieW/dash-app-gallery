import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__, description="How to make an interactive heatmap with a Checklist"
)

filename = __name__.split("pages.")[1]


notes = """

#### Plotly Documentation:  

- [Heatmaps](https://plotly.com/python/heatmaps/)


#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""

layout = example_app(filename, notes=notes)
