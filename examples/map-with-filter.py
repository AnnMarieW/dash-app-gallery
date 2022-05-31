import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash import Dash, html, dcc, Output, Input, State, ALL
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


df = pd.read_csv(
    "https://raw.githubusercontent.com/IcToxi/datasets/main/AB_NYC_2019.csv"
).rename(columns={"longitude": "lon", "latitude": "lat"})


app = Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ, dbc.icons.BOOTSTRAP])


app.layout = html.Div(
    [
        dl.Map(
            children=[
                dl.TileLayer(),
                rooms_geo := dl.GeoJSON(cluster=True, zoomToBoundsOnClick=True),
            ],
            style={
                "width": "100%",
                "height": "100%",
                "position": "absolute",
                "zIndex": 1,
            },
            center=[40.730610, -73.935242],
            zoom=12,
        ),
        html.Div(
            [
                btn := dbc.Button(
                    [html.I(className="bi bi-info-circle-fill me-2"), "Filter"],
                    color="info",
                    className="me-1",
                    style={"zIndex": 10, "position": "absolute"},
                ),
            ],
            className="pt-2 me-2 d-grid d-md-flex justify-content-md-end",
        ),
        drawer := dbc.Offcanvas(
            html.Div(
                [
                    html.Strong("Room Type:", className="text-secondary"),
                    dbc.Checklist(
                        id={"type": "filter", "index": "room_type"},
                        className="btn-group mt-2 mb-2",
                        inputClassName="btn-check",
                        labelClassName="btn btn-outline-primary",
                        labelCheckedClassName="active",
                        options=[
                            {"label": i, "value": i} for i in df.room_type.unique()
                        ],
                        value=df.room_type.unique(),
                    ),
                    html.Strong("Price Range:", className="text-secondary"),
                    price_dist := dcc.Graph(
                        className="mt-2 mb-3", config=dict(displayModeBar=False)
                    ),
                    dcc.RangeSlider(
                        id={"type": "filter", "index": "price_range"},
                        min=df.price.min(),
                        max=df.price.max(),
                        value=[df.price.min(), df.price.max()],
                        tooltip={"placement": "bottom"},
                    ),
                ]
            ),
            close_button=False,
            style={"width": "45%"},
            class_name="bg-black",
        ),
    ],
)

app.clientside_callback(
    "((n, is_open) => n ? !is_open : is_open)",
    Output(drawer, "is_open"),
    Input(btn, "n_clicks"),
    State(drawer, "is_open"),
)


@app.callback(
    Output(price_dist, "figure"),
    Input({"type": "filter", "index": "price_range"}, "value"),
)
def update_graph(_range):
    selected = (_range[0] <= df.price) & (df.price <= _range[1])
    selected.name = "selected"
    _df = pd.concat([df.price, selected], axis=1)
    fig = px.histogram(
        _df, x="price", color="selected", color_discrete_map={1: "tomato", 0: "gray"}
    )
    fig.update_layout(
        xaxis=dict(ticks="", showticklabels=False, showgrid=False, zeroline=False),
        yaxis=dict(ticks="", showticklabels=False, showgrid=False, zeroline=False),
        paper_bgcolor="black",
        plot_bgcolor="black",
        height=150,
        xaxis_title=None,
        yaxis_title=None,
        showlegend=False,
        margin=dict(l=0, r=0, t=0, b=0),
    )
    return fig


@app.callback(
    Output(rooms_geo, "data"),
    Input({"type": "filter", "index": ALL}, "value"),
    State({"type": "filter", "index": ALL}, "id"),
)
def update_map(value, _id):
    params = {i["index"]: v for i, v in zip(_id, value)}

    rooms = df.query(
        f"{params['price_range'][0]} <= price & price <= {params['price_range'][1]} & room_type in {params['room_type']}"
    ).to_dict("records")

    geojson = dlx.dicts_to_geojson(
        [
            {
                **room,
                **dict(
                    tooltip=" | ".join(
                        f"${room[i]}" if i == "price" else str(room[i])
                        for i in ["name", "host_name", "room_type", "price"]
                    )
                ),
            }
            for room in rooms
        ]
    )
    return geojson


if __name__ == "__main__":
    app.run_server(debug=True)
