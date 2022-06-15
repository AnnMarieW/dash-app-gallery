import dash
from utils.code_and_show import example_app

dash.register_page(
    __name__,
    description="Two tabs that plot the Iris and Gapminder data on a bubble chart and scatter graph",
)

filename = __name__.split("pages.")[1]

layout = example_app(filename)
