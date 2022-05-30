import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Plotting data from csv file")

filename = __name__.split("pages.")[1]


notes = """
### For more information see:
Plotly docs:  

- [How plot data from csv file](https://plotly.com/python/plot-data-from-csv/)


### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
