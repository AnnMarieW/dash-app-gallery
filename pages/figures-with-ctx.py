import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app changes a figure using callback_context (CTX). It has a side-by-side layout and a ctx-callback.",
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [Callback Context](https://dash.plotly.com/determining-which-callback-input-changed)

#### Plotly Documentation:
- [Bar charts](https://plotly.com/python/bar-charts/)
- [Line charts](https://plotly.com/python/line-charts/)
- [Filled Area Plots](https://plotly.com/python/filled-area-plots/)

#### Community Components:

Dash Bootstrap Components 
- [Button](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/button/ "This component was made by the community and not officially maintained by Plotly.")

##### Contributed by:
This example app was contributed by [tolgahancepel](https://github.com/tolgahancepel)
"""

layout = example_app(filename, notes=notes)
