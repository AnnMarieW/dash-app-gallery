import dash

from utils.code_and_show import example_app


dash.register_page(
    __name__, description="This app does Analysis of the ML model's results using ROC and PR curves. This app uses top-down layout with regular callback."
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:
- [Dropdown](https://dash.plotly.com/dash-core-components/dropdown)


#### Plotly Documentation:  
- [ROC and PR Curves](https://plotly.com/python/roc-and-pr-curves/)
Interpret the results of your classification using Receiver Operating Characteristics (ROC) and Precision-Recall (PR) Curves 
- [area](https://plotly.com/python/filled-area-plots/)


#### Community Components:

#### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)
