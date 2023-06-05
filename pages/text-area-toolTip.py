import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This application shows the Text Area component along with the Tooltip. It has a top-bottom layout and regular-callback.",
)

filename = __name__.split("pages.")[1]

# any notes will be displayed below the code-and-show page in a dcc.Markdown component
notes = """
#### Dash Components in App:
- [Markdown](https://dash.plotly.com/dash-core-components/markdown)

#### Community Components:

Dash Tool Tips
- [Tooltips] (https://dash.plotly.com/datatable/tooltips "This component was made by the community and not officially maintained by Plotly.")

Dash Mantine Components
- [Textarea](https://dash.plotly.com/dash-html-components/textarea "This component was made by the community and not officially maintained by Plotly.")


##### Contributed by:
This example app was contributed by [Sangeetha Venkatesan](https://github.com/SangeethaVenkatesan)
"""

layout = example_app(filename, notes=notes)
