import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__, description="Compare three regression models to predict revenue"
)

filename = __name__.split("pages.")[1]


notes = """

#### Plotly Documentation:  

- [Visualize regression in scikit-learn](https://plotly.com/python/ml-regression/)


#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
