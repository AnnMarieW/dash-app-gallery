from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

iris = px.data.iris()
gapminder = px.data.gapminder()
tips = px.data.tips()
carshare = px.data.carshare()

figure_templates = [
    "plotly",
    "ggplot2",
    "seaborn",
    "simple_white",
    "plotly_white",
    "plotly_dark",
    "presentation",
    "xgridoff",
    "ygridoff",
    "gridon",
    "none",
]

change_figure_template = html.Div(
    [
        html.Div("Change Figure Template"),
        dcc.Dropdown(figure_templates, figure_templates[0], id="template-change-x-template"),
    ],
    className="pb-4",
)


app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(change_figure_template, lg=6)),
        dbc.Row(dbc.Col(html.Div(id="template-change-x-graphs"))),
    ],
    className="dbc p-4",
    fluid=True,
)


@app.callback(
    Output("template-change-x-graphs", "children"),
    Input("template-change-x-template", "value"),
)
def update_graph_theme(template):
    graph1 = dcc.Graph(
        figure=px.scatter(
            iris,
            x="sepal_width",
            y="sepal_length",
            color="species",
            title=f"Iris <br>{template} figure template",
            template=template,
        ),
        className="border",
    )
    graph2 = dcc.Graph(
        figure=px.scatter(
            gapminder,
            x="gdpPercap",
            y="lifeExp",
            size="pop",
            color="continent",
            hover_name="country",
            animation_frame="year",
            animation_group="country",
            log_x=True,
            size_max=60,
            title=f"Gapminder <br>{template} figure template",
            template=template,
        ),
        className="border",
    )
    graph3 = dcc.Graph(
        figure=px.violin(
            tips,
            y="tip",
            x="smoker",
            color="sex",
            box=True,
            points="all",
            hover_data=tips.columns,
            title=f"Tips <br>{template} figure template",
            template=template,
        ),
        className="border",
    )
    graph4 = dcc.Graph(
        figure=px.scatter_mapbox(
            carshare,
            lat="centroid_lat",
            lon="centroid_lon",
            color="peak_hour",
            size="car_hours",
            size_max=15,
            zoom=10,
            mapbox_style="carto-positron",
            title=f"Carshare <br> {template} figure template",
            template=template,
        ),
        className="border",
    )

    return [
        dbc.Row([dbc.Col(graph1, lg=6), dbc.Col(graph2, lg=6)]),
        dbc.Row([dbc.Col(graph3, lg=6), dbc.Col(graph4, lg=6)], className="mt-4"),
    ]


if __name__ == "__main__":
    app.run_server(debug=True)
