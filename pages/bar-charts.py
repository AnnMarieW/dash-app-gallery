import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="Bar Chart with a Dropdown",
    callback_dd="1 Output 1 Input",
)

filename = __name__.split("pages.")[1]


def layout():
    return example_app(f"pages/examples/{filename}.py")
