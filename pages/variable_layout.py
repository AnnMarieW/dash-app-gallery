
import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="This application shows Line chart, DataTable and dropdown. It has a side-by-side layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [DataTable](https://dash.plotly.com/datatable)
- [Download](https://dash.plotly.com/dash-core-components/download)

#### Plotly Documentation:  
- [Line Chart](https://plotly.com/python/line-charts/)

#### Community Components:

Dash Mantine Components 
- [SimpleGrid](https://www.dash-mantine-components.com/components/simplegrid "This component was made by the community and not officially maintained by Plotly.")

##### Contributed by:
This example app was contributed by [Milan Mitrovic](https://milanzmitrovic.github.io)
"""

layout = example_app(filename, notes=notes)


