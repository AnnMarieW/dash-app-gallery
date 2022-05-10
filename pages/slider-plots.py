import dash

from utils.code_and_show import example_app


dash.register_page(__name__, 
    description = "This app plots the iris data on a bar chart filtered by a slider.",
    layout_type = "top bottom",
    components_type = ["slider"],
    graph_type = "bar", 
    callback_type = "general"
)

filename = __name__.split("pages.")[1]

# make a mini layout with the links to the docs that would go under each app
# all_links: {"slider": "https://dash.plotly.com/dash-core-components/slider",
# "bar": "https://plotly.com/python/bar-charts/"} 
# links = html.Div([all_links])


def layout():
    return example_app(filename)
