import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="Iris samples filtered by petal width with a slider",
    callback_dd="1 Output 1 Input",
)

filename = __name__.split("pages.")[1]


notes = """

#### Plotly documentation:  

- [3d Scatter Plots](https://plotly.com/python/3d-scatter-plots/)


##### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
