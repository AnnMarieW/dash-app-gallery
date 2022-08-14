
import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This application shows an Icicle chart, modal and dropdown. It has a top-bottom layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [Dropdown](https://dash.plotly.com/dash-core-components/dropdown)
- [DatePickerRange](https://dash.plotly.com/dash-core-components/datepickerrange)

#### Plotly Documentation:  
- [Icicle Chart](https://plotly.com/python/icicle-charts/)

#### Community Components:

Dash Bootstrap Components 
- [Button](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/button/ "This component was made by the community and not officially maintained by Plotly.")
- [Offcanvas](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/offcanvas/ "This component was made by the community and not officially maintained by Plotly.")

##### Contributed by:
This example app was contributed by [Milan Mitrovic](https://milanzmitrovic.github.io)
"""

layout = example_app(filename, notes=notes)

