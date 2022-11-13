import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="Project management app with a DataTable and a Gantt chart. This app has a top-bottom layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]


notes = """
#### Dash Components in App:  
- [DataTable](https://dash.plotly.com/datatable)

#### Plotly Documentation:  
- [Gantt Timeline Plots](https://plotly.com/python/gantt/)

#### Contributed by:
This example app was contributed by [@asaf95 Asaf Ben-Menachem](https://github.com/Asaf95)

"""


layout = example_app(filename, notes=notes)
