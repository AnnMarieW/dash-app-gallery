import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This application demonstrates the use of html.Img and dbc.Modal through the F.L.A.M.E game. It has a top-bottom layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]

notes = """

#### Dash Components in App:  
- [Input](https://dash.plotly.com/dash-core-components/input)
- [Img](https://dash.plotly.com/dash-html-components/img)
- [Markdown](https://dash.plotly.com/dash-core-components/markdown)

#### Community Components:
Dash Bootstrap Components 
- [Modal](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/modal/)
- [Button](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/button/)

#### Contributed by:
This example app was contributed by [Someshfengde](https://github.com/someshfengde)

"""


layout = example_app(filename, notes=notes)
