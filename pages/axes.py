import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="Interactive Plotly Axes Labels",
    callback_dd="1 Output 1 Input",
)

filename = __name__.split("pages.")[1]


layout = example_app(filename)
