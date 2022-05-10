import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description = "This app connects between a sunburst plot and three chained callbacks",
    layout_type = "side by side",
    components_type = ["dropdown"],
    graph_type = "sunburst",
    callback_type = "chained"
)

filename = __name__.split("pages.")[1]

# make a mini layout with the links to the docs that would go under each app
# all_links = {"dropdown: https://dash.plotly.com/dash-core-components/dropdown",
# "chained callback": "https://dash.plotly.com/basic-callbacks#dash-app-with-chained-callbacks",
# "sunburst": "https://plotly.com/python/sunburst-charts/"} 
# links = html.Div([all_links])

def layout():
    return example_app(filename)
