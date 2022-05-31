import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="How to fill the area enclosed by traces.")

filename = __name__.split("pages.")[1]


notes = """
### For more information see:
Plotly docs:  

- [Filled area charts](https://plotly.com/python/filled-area-plots/)


### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""

layout = example_app(filename, notes=notes)
