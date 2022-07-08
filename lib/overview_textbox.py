from dash import dcc
import dash_bootstrap_components as dbc

content = """
Welcome to the Dash Examples Index!


"""



card = dbc.Card(
    dcc.Markdown(content),
    style={"height": 250, "overflow": "auto"},
    className="shadow-sm p-4 mt-4 mx-2",
)
