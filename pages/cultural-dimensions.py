import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app uses tabs to highlight cultural dimensions on a bar chart.",
)

filename = __name__.split("pages.")[1]

# make a mini layout with the links to the docs that would go under each app
# links = html.Div([])

layout = example_app(filename)
