import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Visualization of PCA's explained variance")

filename = __name__.split("pages.")[1]


notes = """
### For more information see:
Plotly docs:  

- [Visualize Principle Component Analysis (PCA) of your high-dimensional data](https://plotly.com/python/pca-visualization/)


### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
