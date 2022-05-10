import dash
from utils.code_and_show import example_app

dash.register_page(
    __name__,
    description = "An app that plots the Iris data set combined with the checklist",
    layout_type = "general",
    components_type  = "checklist",
    graph_type = "scatter",
    callback_type  = "general",
)

filename = __name__.split("pages.")[1]

def layout():
    return example_app(filename)
