from dash import Dash, html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

df = px.data.wind()
df[["min_strength", "max_strength"]] = (
    df.strength.str.replace(r"6\+", "6-7").str.split("-", expand=True).astype(int)
)

dropdown_1 = dbc.Select(
    options=[{"label": v, "value": v.lower()} for v in ("Bar", "Line")],
    value="bar",
    required=True,
)

range_1 = dcc.RangeSlider(
    0,
    7,
    step=1,
    marks={**{v: str(v) for v in range(7)}, 7: ">6"},
)

graph_1 = dcc.Graph(responsive=True)

app.layout = dbc.Container(
    [
        html.H1("Windy wind things"),
        html.Div(
            children=[
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.P(
                                    "The chart illustrates the distribution of wind speeds by direction, "
                                    "revealing a significant bias towards winds originating from the west. "
                                    "This notable preponderance of westerly winds suggests the influence of "
                                    "macro-scale climatic patterns, such as prevailing westerlies common in "
                                    "mid-latitude regions. Higher wind speeds are predominantly clustered "
                                    "within the western sector, indicating that stronger wind events mostly "
                                    "come from this direction. This pattern could be reflective of regional "
                                    "topographical influences or larger synoptic systems driving westerly flows."
                                ),
                                dbc.Label("Filter wind intensity"),
                                range_1,
                                dbc.Label("Select chart type"),
                                dropdown_1,
                            ],
                            lg=4,
                        ),
                        dbc.Col(
                            graph_1,
                            lg=8,
                        ),
                    ]
                )
            ],
        ),
    ]
)


@callback(
    Output(graph_1, "figure"), Input(range_1, "value"), Input(dropdown_1, "value")
)
def update_figure(strength_range, graph_type):
    df_copy = df.copy()

    if strength_range:
        start, stop = min(strength_range), max(strength_range)
        df_copy = df_copy[(df.min_strength >= start) & (df.max_strength <= stop)]

    additional_args = {}
    match graph_type.lower():
        case "bar":
            func = px.bar_polar
        case "line":
            func = px.line_polar
            additional_args["line_close"] = True

    fig = func(
        df_copy,
        r="frequency",
        theta="direction",
        color="strength",
        template="plotly_dark",
        color_discrete_sequence=px.colors.sequential.Plasma_r,
        **additional_args,
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
