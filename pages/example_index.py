import dash
import lib.example_index

dash.register_page(
    __name__,
    title="Dash Example Index",
    description="This community-supported project is designed for people new to Plotly and Dash. It contains minimal sample apps with ~150 lines of code to demonstrate basic usage of graphs, components, callbacks, and layout design.",
    image="overview.png",
    layout=lib.example_index.layout,
)
