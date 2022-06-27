import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="Interactive box plot with Checklist and RadioItems. It has a top-bottom layout and a regular-callback",
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:  
- [Dcc.RadioItems](https://dash.plotly.com/dash-core-components/radioitems)
- [Dcc.Checklist](https://dash.plotly.com/dash-core-components/checklist)

#### Plotly Documentation:  
- [Box Plots](https://plotly.com/python/box-plots/)

A box plot is a statistical representation of the distribution of a variable through its quartiles. 
The ends of the box represent the lower and upper quartiles, while the median (second quartile) is marked by a line inside the box. 


#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
