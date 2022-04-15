import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description = "Dash Sample App",
    layout_type = "1 Row 1 Col",
    graph = "Choropleth",
    # callback = "None"
)

filename = __name__.split("pages.")[1]


def layout():
    return example_app(f"pages/examples/{filename}.py")
