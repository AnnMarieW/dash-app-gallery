import dash
from dash import html, dcc

from utils.code_and_show import example_app



dash.register_page(
    __name__,
    description = "This app plots a Poisson distribution on a histogram, which contains a formula with MathJax.",
    layout_type = "cards",
    components_type = ["input", "card", "accordion", "markdown"],
    graph_type = "histogram",
    callback_type = "general",
)

filename = __name__.split("pages.")[1]

# make a mini layout with the links to the docs that would go under each app
# all_links: {"input": "https://dash.plotly.com/dash-core-components/input",
# "card": "https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/",
# "accordion": "https://dash-bootstrap-components.opensource.faculty.ai/docs/components/accordion/",
# "markdown": "https://dash.plotly.com/dash-core-components/markdown",
# "histogram": "https://plotly.com/python/histograms/"}
# links = html.Div([all_links])


# any notes will be displayed below the code-and-show page in a dcc.Markdown component
notes = """
### For more information see:
Dash docs:  

- [Input component](https://dash.plotly.com/dash-core-components/input)
- [Markdown component](https://dash.plotly.com/dash-core-components/markdown)

Plotly docs:  

- [histogram](https://plotly.com/python/histograms/) 

Dash Bootstrap Components docs:
- [Card](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/)
- [Accordion](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/accordion/)


### Contributed by:
This example app was contributed by [name](link)

"""

def layout():
    return html.Div(
        [
            example_app(f"pages/examples/{filename}.py"),
            dcc.Markdown(notes, className="m-4")
        ]
    )
