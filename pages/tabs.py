import dash
from utils.code_and_show import example_app

dash.register_page(
    __name__,
    description = "Two tabs that plot the Iris and Gapminder data on a bubble chart and scatter graph",
    layout_type = "tabs",
    components_type  = ["tabs"],
    graph_type = ["scatter", "bubble"],
    callback_type  = "None",
)

filename = __name__.split("pages.")[1]

def layout():
    return example_app(f"pages/examples/{filename}.py")


