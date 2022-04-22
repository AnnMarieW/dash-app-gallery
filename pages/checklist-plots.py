from utils.code_and_show import example_app

dash.register_page(
￼    __name__,
￼    description = "Dash Sample App",
￼    layout_type = "2Row():1Col()",
￼    graph = "scatter",
    components = "checklist",
￼    callback = "1input:1output",
    dataset = "iris"
￼)
￼
￼filename = __name__.split("pages.")[1]
