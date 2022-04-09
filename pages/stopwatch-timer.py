import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="stopwatch timer application with 2 buttons ")


def layout():
    return example_app(f"pages/examples/stopwatch.py")