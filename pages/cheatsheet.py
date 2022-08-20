from dash import register_page

from examples.cheatsheets import cheatsheet_layout

register_page(__name__, layout=cheatsheet_layout.layout, description="Dash Cheatsheet")