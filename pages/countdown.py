import dash

from lib.code_and_show import example_app

dash.register_page(
    __name__,
    description="This app connects a button with the LEDDisplay to generate a stopwatch with an mp3 alarm sound at the end. It has a top-down layout with a regular-callback.",
)

filename = __name__.split("pages.")[1]

notes = """

#### Dash Components in App:
- [Interval](https://dash.plotly.com/dash-core-components/interval)
- [Store](https://dash.plotly.com/dash-core-components/store)
- [Input](https://dash.plotly.com/dash-core-components/input)
- [LEDDisplay](https://dash.plotly.com/dash-daq/leddisplay)
- [Audio](https://dash.plotly.com/dash-html-components/audio)

#### Community Components:
Dash Bootstrap Components 
- [Button component](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/button/ "This component was made by the community and not officially maintained by Plotly.")

##### Contributed by:
This example app was contributed by [Tuomas](https://github.com/tuopouk)

"""

layout = example_app(filename, notes=notes)
