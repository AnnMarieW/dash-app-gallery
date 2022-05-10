import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Dash Sample App")

filename = __name__.split("pages.")[1]


def layout():
    return example_app(filename)
