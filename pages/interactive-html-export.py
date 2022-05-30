import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="How to save interactive HTML versions of your figures to your local disk.",
)

filename = __name__.split("pages.")[1]


notes = """
### For more information see:
Plotly docs:  

- [Saving interactive HTML versions of your figures to your local disk. ](https://plotly.com/python/interactive-html-export/)


### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""

layout = example_app(filename, notes=notes)
