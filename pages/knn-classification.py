import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="Visualize scikit-learn's k-Nearest Neighbors (kNN) classification",
)

filename = __name__.split("pages.")[1]


notes = """
### For more information see:
Plotly docs:  

- [Visualize scikit-learn's k-Nearest Neighbors (kNN) classification](https://plotly.com/python/knn-classification/)


### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""

layout = example_app(filename, notes=notes)
