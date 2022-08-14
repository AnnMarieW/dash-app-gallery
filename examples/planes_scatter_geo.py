from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df_airports = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv"
)

app = Dash(__name__)


app.layout = html.Div(
    [
        html.H4("Airports"),
        html.P(
            "px.scatter_geo is used to plot points on globe across geolocations while "
            "px.scatter_mapbox is used to plot points on map across geolocations."
        ),
        dcc.Graph(id="planes_scatter_geo-x-graph"),
        html.P(
            "Enter the type of graph you want to plot: (scatter_geo or scatter_mapbox)"
        ),
        dcc.Dropdown(
            id="planes_scatter_geo-x-type",
            options=["scatter_mapbox", "scatter_geo"],
            value="scatter_mapbox",
            clearable=False,
        ),
    ]
)


@app.callback(
    Output("planes_scatter_geo-x-graph", "figure"),
    Input("planes_scatter_geo-x-type", "value"),
)
def generate_chart(values):
    if values == "scatter_geo":
        # changing so that the default position will be US
        fig = px.scatter_geo(
            df_airports,
            locationmode="USA-states",
            lat="lat",
            lon="long",
            hover_data=["airport", "city", "state", "cnt"],
            color="cnt",
            color_continuous_scale=px.colors.cyclical.IceFire,
            projection="orthographic",
        )

        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    else:
        fig = px.scatter_mapbox(
            df_airports,
            lat="lat",
            lon="long",
            hover_data=["airport", "city", "state", "cnt"],
            size="cnt",
            color="cnt",
            zoom=3,
        )
        fig.update_layout(mapbox_style="open-street-map")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
