import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Discrete and continuous color scales")

filename = __name__.split("pages.")[1]


notes = """

#### Plotly Documentation:  

- [Creating and updating figures](https://plotly.com/python/discrete-color/)
How to use and configure discrete color sequences, also known as categorical or qualitative color scales.


#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
