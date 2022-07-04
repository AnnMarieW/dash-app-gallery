import dash

from lib.code_and_show import example_app


dash.register_page(__name__, description="This app shows visualization of PCA's explained variance. It has a top-bottom layout and a regular-callback.")

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:
- [Slider](https://dash.plotly.com/dash-core-components/slider)

#### Plotly Documentation:  
- [Visualize Principle Component Analysis (PCA) of your high-dimensional data](https://plotly.com/python/pca-visualization/)
- [Scatterplot Matrix](https://plotly.com/python/splom/)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)
"""


layout = example_app(filename, notes=notes)
