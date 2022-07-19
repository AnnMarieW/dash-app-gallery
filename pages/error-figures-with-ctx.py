import dash
from dash import html

from lib.code_and_show import example_app


dash.register_page(__name__)

filename = __name__.split("pages.")[1]
no_error = filename.split("-")[1:]
no_error = "-".join(no_error)


layout = html.Div([html.H4("Error App"),example_app(filename), html.H4("Corrected App"), example_app(no_error) ])
