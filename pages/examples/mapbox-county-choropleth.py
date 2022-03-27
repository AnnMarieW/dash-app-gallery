from dash import Dash, dcc, html, Input, Output
import plotly.express as px

token = open(".mapbox_token").read()  # you will need your own token


app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Polotical candidate voting pool analysis"),
        html.P("Select a candidate:"),
        dcc.RadioItems(
            id="mapbox-county-choropleth-x-candidate",
            options=["Joly", "Coderre", "Bergeron"],
            value="Coderre",
            inline=True,
        ),
        dcc.Graph(id="mapbox-county-choropleth-x-graph"),
    ]
)


@app.callback(
    Output("mapbox-county-choropleth-x-graph", "figure"),
    Input("mapbox-county-choropleth-x-candidate", "value"),
)
def display_choropleth(candidate):
    df = px.data.election()  # replace with your own data source
    geojson = px.data.election_geojson()

    fig = px.choropleth_mapbox(
        df,
        geojson=geojson,
        color=candidate,
        locations="district",
        featureidkey="properties.district",
        center={"lat": 45.5517, "lon": -73.7073},
        zoom=9,
        range_color=[0, 6500],
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, mapbox_accesstoken=token)

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
