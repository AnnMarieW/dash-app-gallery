import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="Graph visualizations on the data scientists salery.It has a side-by-side layout with ctx .",
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [Radioitems](https://dash.plotly.com/dash-core-components/radioitems)

#### Plotly Documentation:  
- [choropleth-maps](https://plotly.com/python/choropleth-maps/)
- [bar](https://plotly.com/python/bar-charts/)
- [line](https://plotly.com/python/line-charts/)


#### Community Components:
Dash Bootstrap Components 
- [Container](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/"This component was made by the community and not officially maintained by Plotly.")


##### Contributed by:
This example app was contributed by [Someshfengde](https://www.github.com/someshfengde)
"""

layout = example_app(filename, notes=notes)