from dash import dcc
import dash_bootstrap_components as dbc

content = """
### Welcome to the Dash Example Index 

This is a community-supported project designed for people new to Plotly and Dash. It contains minimal sample apps with ~150 lines of code to demonstrate basic usage of graphs, components, callbacks, and layout design. 

If you have any suggestions for improvements, please open a [new issue](https://github.com/AnnMarieW/dash-app-gallery/issues).
If you would like to contribute your own app, checkout the [contributing guide](https://github.com/AnnMarieW/dash-app-gallery/blob/main/CONTRIBUTING.md). 

"""



card = dbc.Card(
    dcc.Markdown(content, link_target="_blank"),
    style={"height": 250, "overflow": "auto"},
    className="shadow-sm p-4 mt-4 mx-2",
)
