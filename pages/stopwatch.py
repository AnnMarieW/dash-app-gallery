import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description = "Stopwatch timer application with 1 button and an input field.",
    layout_type = "general",
    components_type = ["leddisplay", "input", "interval", "powerbutton"],
    graph_type = "none", 
    callback_type = "general"
)

filename = __name__.split("pages.")[1]

# make a mini layout with the links to the docs that would go under each app
# all_links: {"input": "https://dash.plotly.com/dash-core-components/input",
# "interval": "https://dash.plotly.com/dash-core-components/interval",
# "dash-daq": "https://dash.plotly.com/dash-daq"} 
# links = html.Div([all_links])


def layout():
    return example_app(f"pages/examples/{filename}.py")
