import dash

from lib.code_and_show import example_app

dash.register_page(
    __name__,
    description="This application updates traces of a Graph component every 25ms with the clientside callback. It has a top-bottom layout and a clientside-callback.",
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [Interval](https://dash.plotly.com/dash-core-components/interval)
- [Store](https://dash.plotly.com/dash-core-components/store)
- [Clientside Callback](https://dash.plotly.com/clientside-callbacks)

##### Contributed by:
This example app was contributed by [Emil](https://github.com/emilhe)
"""

layout = example_app(filename, notes=notes)