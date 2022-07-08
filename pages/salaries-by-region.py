import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This application includes an example of a 3d line chart with a dropdown. This app uses side-by-side layout with a regular-callback",
)

filename = __name__.split("pages.")[1]

# any notes will be displayed below the code-and-show page in a dcc.Markdown component
notes = """
#### Dash Components in App:
- [Dropdown](https://dash.plotly.com/dash-core-components/dropdown)

#### Plotly Documentation:
- [3d-Line Plot](https://plotly.com/python/3d-line-plots/)

##### Contributed by:
This example app was contributed by [tolgahancepel](https://github.com/tolgahancepel)
"""

layout = example_app(filename, notes=notes)
