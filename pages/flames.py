import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    order=0,
    description="This application demonstrates the use of Img and dbc Modal. It has a top-bottom layout and a regular-callback and modal container.",
)

filename = __name__.split("pages.")[1]

notes = """

#### Dash Components in App:  
- [dcc input](https://dash.plotly.com/dash-core-components/input)
- [Button](https://dash.plotly.com/dash-html-components/button)
- [html img](https://dash.plotly.com/dash-html-components/img)
- [Markdown](https://dash.plotly.com/dash-core-components/markdown)

#### Dash Bootstrap Components:
- [dbc Modal](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/modal/)

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
