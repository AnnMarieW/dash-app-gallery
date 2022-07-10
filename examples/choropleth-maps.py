from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = px.data.election()

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Political candidate voting pool analysis"),
        html.P("Select a candidate:"),
        dcc.RadioItems(
            id="choropleth-maps-x-candidate",
            options=["Joly", "Coderre", "Bergeron"],
            value="Coderre",
            inline=True,
        ),
        dcc.Graph(id="choropleth-maps-x-graph"),
    ]
)


@app.callback(
    Output("choropleth-maps-x-graph", "figure"),
    Input("choropleth-maps-x-candidate", "value"),
)
def display_choropleth(candidate):
    geojson = px.data.election_geojson()
    fig = px.choropleth(
        df,
        geojson=geojson,
        color=candidate,
        locations="district",
        featureidkey="properties.district",
        projection="mercator",
        range_color=[0, 6500],
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
