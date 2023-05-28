"""
This defines the feature apps component.

Each feature app category is a`dbc.AccordionItem`. This component contains  buttons formatted as links.

There is one dictionary for each category, e.g. `figure_type`
This dictionary is used to create the link buttons, the keys are the link name, and the values are the search terms
that will be used to filter the code files.

The search terms are passed to the callback via the "index" of a pattern matching dict id
  e.g. ` id = {"type": "feature_app", "index": searchterm}

"""
from dash import html

import dash_bootstrap_components as dbc


figure_type = {
    # key  : value
    # name of link  : search term used to filter the code files
    "Scatter": "px.scatter",
    "Line": "px.line",
    "3d Scatter": "px.scatter_3d",
    "3d Line": "px.line_3d",
    "Bar": "px.bar",
    "Box": "px.box",
    "Candlestick": "go.Candlestick",
    "Choropleth": "px.choropleth",
    "ECDF Plots": "px.ecdf",
    "Histogram": "px.histogram",
    "Icicle": "px.icicle",
    "Filled Area": "px.area",
    "Contour": "go.Contour",
    "Parallel Coordinates": "px.parallel_coordinates",
    "Scatter Matrix": "px.scatter_matrix",
    "Pie": "px.pie",
    "Scatter Geo": "px.scatter_geo",
    "Scatter Map": "px.scatter_mapbox",
    "Sankey": "go.Sankey",
    "Sub plots": "make_subplots",
    "Sunburst": "px.sunburst",
    "Timeline": "px.timeline",
    "Line Geo": "px.line_geo",
    "Violin": "px.violin",
}
figure_type = {key: figure_type[key] for key in sorted(figure_type)}

callback_type = {
    # key  : value
    # name of link  : search term used to filter the code files
    "Pattern Match": "pattern matching",
    "Clientside": "clientside_callback",
    "Callbacks": "callback(",
    "Callback context (ctx)": "ctx",
    "Chained": "chained",
}

components = {
    # key  : value
    # name of link  : search term used to filter the code files
    "Boolean Switch": "daq.BooleanSwitch",
    "Date Picker": "DatePicker",
    "Cards": "Card",
    "Dash DataTable": "DataTable",
    "Dropdown": "Dropdown(",
    "Checklist": "Checklist(",
    "Tabs": "Tab(",
    "Slider": "Slider(",
    "Cytoscape": "Cyto",
    "Download": "Download",
    "Alert": "Alert(",
    "Button": "Button(",
    "Clipboard": "Clipboard(",
    "Accordion": "Accordion",
    "Loading": "Loading",
    "Markdown": "Markdown",
    "Input": "dcc.Input",
    "Interval": "Interval",
    "Color Picker": "daq.Color",
    "Led display": "daq.LED",
    "Power Button": "daq.Power",
    "RadioItems": "RadioItems",
    "Offcanvas": "dbc.Offcanvas",
    "Modal": "dbc.Modal",
    "Store": "dcc.Store",
    "AgGrid": "AgGrid"
}
components = {key: components[key] for key in sorted(components)}


feature_app_div = html.Div(
    [
        dbc.Label("Featured Examples", className="fw-bolder"),
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    [
                        dbc.Button(
                            name,
                            id={"type": "feature_app", "index": searchterm},
                            color="link",
                        )
                        for name, searchterm in figure_type.items()
                    ],
                    title="Figures",
                ),
                dbc.AccordionItem(
                    [
                        dbc.Button(
                            name,
                            id={"type": "feature_app", "index": searchterm},
                            color="link",
                        )
                        for name, searchterm in callback_type.items()
                    ],
                    title="Callbacks",
                ),
                dbc.AccordionItem(
                    [
                        dbc.Button(
                            name,
                            id={"type": "feature_app", "index": searchterm},
                            color="link",
                        )
                        for name, searchterm in components.items()
                    ],
                    title="Components",
                ),
            ],
            start_collapsed=True,
            id="featured-apps",
        ),
    ]
)
