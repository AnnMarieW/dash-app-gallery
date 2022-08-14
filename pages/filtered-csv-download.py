import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="Gapminder data in a DataTable filtered by year with a RangeSlider. Includes an option to download the filtered data as a csv file.",
)

filename = __name__.split("pages.")[1]

notes = """
#### Dash Components in App:
- [DataTable](https://dash.plotly.com/datatable)
- [RangeSlider](https://dash.plotly.com/dash-core-components/rangeslider)
- [Download](https://dash.plotly.com/dash-core-components/download)



##### Contributed by:
This example app was contributed by [tolgahancepel](https://github.com/tolgahancepel)
"""

layout = example_app(filename, notes=notes)
