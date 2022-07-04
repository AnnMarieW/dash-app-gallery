import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="Visualize scikit-learn's k-Nearest Neighbors (kNN) classification. It has a top-bottom layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]


notes = """

#### Dash Components in App:
- [Slider](https://dash.plotly.com/dash-core-components/slider)

#### Plotly Documentation:
- [Visualize scikit-learn's k-Nearest Neighbors (kNN) classification](https://plotly.com/python/knn-classification/)
- [Scatter Plots](https://plotly.com/python/line-and-scatter/)
- [Contour Plots](https://plotly.com/python/contour-plots/)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""

layout = example_app(filename, notes=notes)
