import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Static and Interactive image download")

filename = __name__.split("pages.")[1]


notes = """

#### Plotly Documentation:  

- [Static image export](https://plotly.com/python/static-image-export/)


#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
