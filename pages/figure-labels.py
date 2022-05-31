import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="Select the color of the title and figure labels with a colorpicker",
)

filename = __name__.split("pages.")[1]


notes = """

#### Plotly Documentation:  

- [Setting the Font, Title, Legend Entries, and Axis Titles.](https://plotly.com/python/figure-labels/)


#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""

layout = example_app(filename, notes=notes)
