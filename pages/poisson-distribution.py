import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description = "This app plots poisson distribution on a histogram, contains a formula with MathJax.",
    layout_type = "3row:1col",
    components_type = ["input", "card"],
    graph_type = "histogram", 
    callback_type = "general"
)

filename = __name__.split("pages.")[1]

# make a mini layout with the links to the docs that would go under each app
# links = html.Div([])

def layout():
    return example_app(f"pages/examples/{filename}.py")
