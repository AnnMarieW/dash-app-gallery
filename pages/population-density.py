import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="Population Density Map by Year",
)

filename = __name__.split("pages.")[1]


layout = example_app(filename)
