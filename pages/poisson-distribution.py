import dash
from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app plots a Poisson distribution on a histogram, which contains a formula with MathJax.It has a top-down layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:

- [Input component](https://dash.plotly.com/dash-core-components/input)
- [Markdown component](https://dash.plotly.com/dash-core-components/markdown)

#### Plotly Documentation:  
- [histogram](https://plotly.com/python/histograms/) 

#### Community Components:

Dash Bootstrap Components 
- [Card](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/)
- [Accordion](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/accordion/)

##### Contributed by:
This example app was contributed by [Tolga](https://github.com/tolgahancepel)
"""

layout = example_app(filename, notes=notes)
