from dash import register_page

from examples import cheatsheet

register_page(__name__, layout=cheatsheet.layout, description="Dash Cheatsheet")