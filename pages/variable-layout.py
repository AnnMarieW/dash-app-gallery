
import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This application highlights the Download component, the line chart, the Dash DataTable, and a few Dash Mantine components. It has a side-by-side layout and a regular-callback.",
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
- [Title](https://www.dash-mantine-components.com/components/title "This component was made by the community and not officially maintained by Plotly.")
- [Button](https://www.dash-mantine-components.com/components/button "This component was made by the community and not officially maintained by Plotly.")
- [MultiSelect](https://www.dash-mantine-components.com/components/multiselect "This component was made by the community and not officially maintained by Plotly.")
- [SimpleGrid](https://www.dash-mantine-components.com/components/simplegrid "This component was made by the community and not officially maintained by Plotly.")

##### Contributed by:
This example app was contributed by [Milan Mitrovic](https://milanzmitrovic.github.io)
"""

layout = example_app(filename, notes=notes)


