import dash


from lib.code_and_show import example_app, make_app_first


dash.register_page(
    __name__,
    description="An app that uses clientside callback to display frames because dcc Interval is activated multiple times per second.",
)

filename = __name__.split("pages.")[1]

# any notes will be displayed below the code-and-show page in a dcc.Markdown component
notes = """

#### Dash documentation:  

- [Interval component](https://dash.plotly.com/dash-core-components/interval)

- [Store component](https://dash.plotly.com/dash-core-components/store)

- [Clientside Callback](https://dash.plotly.com/clientside-callbacks)


#### Contributed by:
This example app was contributed by [IcToxi](https://github.com/IcToxi)

"""

layout = example_app(filename, notes=notes)
