import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__, description="Analysis of the ML model's results using ROC and PR curves"
)

filename = __name__.split("pages.")[1]


notes = """
### For more information see:
Plotly docs:  

- [ROC and PR Curves](https://plotly.com/python/roc-and-pr-curves/)
Interpret the results of your classification using Receiver Operating Characteristics (ROC) and Precision-Recall (PR) Curves 


### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
