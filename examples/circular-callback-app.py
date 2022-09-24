import dash
from dash.dependencies import Input, Output
from dash import dcc, html
import pandas as pd
import plotly.express as px

filepath = "https://raw.githubusercontent.com/plotly/datasets/master/volcano_db.csv"
df = pd.read_csv(filepath, encoding="latin")

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.Header("Geographic Distribution of Volcanoes by Height",
                style={"font-size": "30px"}),
    html.Div('Minimum Volcano Height',
             style={"font-size": "20px"}),
    'Meter ',
    dcc.Input(
        id="circular-callback-x-meter",
        value=2000,
        type="number"
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
    style={"marginLeft": 30, "marginTop": 30, "marginBottom": 30, "marginRight": 30})


@ app.callback(
    Output("circular-callback-x-meter", "value"),
    Output("circular-callback-x-feet", "value"),
    Output('circular-callback-x-map', 'figure'),
    Input("circular-callback-x-meter", "value"),
    Input("circular-callback-x-feet", "value"),
)
def sync_input(meter, feet):
    ctx = dash.callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if input_id == "circular-callback-x-meter":
        feet = None if meter is None else (float(meter) * 3.28084)
    else:
        meter = None if feet is None else (float(feet)/3.28084)
    fig = px.scatter_geo(data_frame=df.loc[df["Elev"] >= meter],
                         lat="Latitude",
                         lon="Longitude",
                         size="Elev",
                         hover_name="Volcano Name",
                         projection="natural earth",
                         width=1300,
                         height=900)
    fig.update_layout()
    return meter, feet, fig


if __name__ == "__main__":
    app.run_server(debug=True)
