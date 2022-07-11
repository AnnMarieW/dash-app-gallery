
import dash

from utils.code_and_show import example_app

dash.register_page(
    __name__,
    description="This application shows Treemap chart with modal and dropdown filter. It has a top-bottom layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [Dropdown](https://dash.plotly.com/dash-core-components/dropdown)
- [Tabs](https://dash.plotly.com/dash-core-components/tabs)
- [DatePickerRange](https://dash.plotly.com/dash-core-components/datepickerrange)

#### Plotly Documentation:  
- [Treemap Chart](https://plotly.com/python/treemaps/)
- [Sunburst Chart](https://plotly.com/python/sunburst-charts/)

#### Community Components:

Dash Bootstrap Components 
- [Modal](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/modal/ "This component was made by the community and not officially maintained by Plotly.")
- [Navbar](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/navbar/)

##### Contributed by:
This example app was contributed by [Milan Mitrovic](https://milanzmitrovic.github.io)
"""

layout = example_app(filename, notes=notes)



