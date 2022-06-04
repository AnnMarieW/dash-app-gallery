import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="Combined statistical representations. Adding box, violin or rug subplot to a histogram ",
)

filename = __name__.split("pages.")[1]


notes = """

#### Plotly Documentation:  

- [Dist plots](https://plotly.com/python/distplot/)
Combined statistical representations with px.histogram
Several representations of statistical distributions are available in plotly, such as histograms,
 violin plots, box plots (see the complete list here). It is also possible to combine several representations in the same plot.
 
 For example, the plotly.express function px.histogram can add a subplot with a different statistical representation 
 than the histogram, given by the parameter marginal.


#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
