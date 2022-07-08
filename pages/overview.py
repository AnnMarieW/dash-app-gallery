import dash
import lib.overview

dash.register_page(
    __name__,
    name="Home - Overview",
    description="Dash Examples Index",
    path="/",
    layout=lib.overview.layout,
)
