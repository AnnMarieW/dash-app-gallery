import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This application demonstrates the use of html.Img and dbc.Modal through the F.L.A.M.E.S theory. It has a top-bottom layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]

notes = """

#### Dash Components in App:  
- [dcc input](https://dash.plotly.com/dash-core-components/input)
- [Button](https://dash.plotly.com/dash-html-components/button)
- [html img](https://dash.plotly.com/dash-html-components/img)
- [Markdown](https://dash.plotly.com/dash-core-components/markdown)

#### Community Components:
Dash Bootstrap Components 
- [dbc Modal](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/modal/)

#### Contributed by:
This example app was contributed by [Someshfengde](https://github.com/someshfengde)

"""


layout = example_app(filename, notes=notes)
