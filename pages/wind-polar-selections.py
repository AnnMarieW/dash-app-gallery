import dash

from lib.code_and_show import example_app, make_app_first


dash.register_page(
    __name__,
    description=(
        "This app uses a RangeSlider and Select input to allow the user to "
        "filter wind events and view 2 different polar chart types. It uses a "
        "simple layout and regular-callback."
    ),
)

filename = __name__.split("pages.")[1]


notes = """

#### Dash Components in the App:
- [RangeSlider](https://dash.plotly.com/dash-core-components/rangeslider)

#### Plotly documentation:
- [Polar Chart](https://plotly.com/python/polar-chart/)

##### Contributed by:
This example app was contributed by [Gareth Maddock](https://github.com/gtm19)

"""


layout = example_app(filename, notes=notes, make_layout=make_app_first)
