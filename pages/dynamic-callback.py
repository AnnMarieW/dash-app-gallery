import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="This application shows how to use chained callbacks with a line graph.",
)

filename = __name__.split("pages.")[1]

# any notes will be displayed below the code-and-show page in a dcc.Markdown component
notes = """
#### Dash Components in App:
- [Dropdown component](https://dash.plotly.com/dash-core-components/dropdown)
- [Chained Callback](https://dash.plotly.com/basic-callbacks#dash-app-with-chained-callbacks)

#### Plotly Documentation:
- [Line chart](https://plotly.com/python/line-charts/)

##### Contributed by:
This example app was contributed by [Milan](https://milanzmitrovic.github.io/)

"""

layout = example_app(filename, notes=notes)
