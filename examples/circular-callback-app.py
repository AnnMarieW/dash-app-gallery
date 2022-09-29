from dash import Dash, dcc, html, Input, Output, ctx
import pandas as pd
import plotly.express as px

filepath = "https://raw.githubusercontent.com/plotly/datasets/master/volcano_db.csv"
df = pd.read_csv(filepath, encoding="latin")

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.Header("Geographic Distribution of Volcanoes by Height",
                style={"font-size": "30px", "textAlign": "center"}),
    html.Div('Minimum Volcano Height',
             style={"font-size": "20px"}),
    'Meter ',
    dcc.Input(
        id="circular-callback-x-meter",
        value=2000,
        type="number",
        step=1
    ),
    ' to Feet ',
    dcc.Input(
        id="circular-callback-x-feet",
        value=6561.68,
        type="number",
    ),
    dcc.Graph(
        id="circular-callback-x-map"
    )
],
    style={"margin": 30}
)


@app.callback(
    Output("circular-callback-x-meter", "value"),
    Output("circular-callback-x-feet", "value"),
    Output('circular-callback-x-map', 'figure'),
    Input("circular-callback-x-meter", "value"),
    Input("circular-callback-x-feet", "value"),
)
def sync_input(meter, feet):
    if ctx.triggered_id == "circular-callback-x-meter":
        feet = None if meter is None else round((float(meter) * 3.28084), 1)
    else:
        meter = None if feet is None else round((float(feet)/3.28084), 0)

    fig = px.scatter_geo(data_frame=df.loc[df["Elev"] >= meter],
                         lat="Latitude",
                         lon="Longitude",
                         size="Elev",
                         hover_name="Volcano Name",
                         projection="natural earth")
    
    return meter, feet, fig


if __name__ == "__main__":
    app.run_server(debug=True)
