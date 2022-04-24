import plotly.express as px
from dash import Dash, dcc, html
from dash import Output, Input
from plotly import data

# Data
df = data.iris()

species = df["species"].unique().tolist()

options = [
    {'label': specie.capitalize(),
     'value': specie} for specie in species]

fig = px.scatter(
        df,
        x="sepal_length",
        y="sepal_width", 
        color="species"
)

color_discrete_map = {d.name: d.marker.color for d in fig.data}

range_x = df["sepal_length"].agg({"min", "max"})
range_y = df["sepal_width"].agg({"min", "max"})
range_x = [range_x["min"]*.9, range_x["max"]*1.1]
range_y = [range_y["min"]*.9, range_y["max"]*1.1]

# App
app = Dash(__name__)

app.layout = html.Div([
    dcc.Checklist(
        options=options,
        labelStyle={'display': 'inline-block'},
        value=species,
        id='checklist-plots-checklist'),
     dcc.Graph(id='checklist-plots-scatter')
])

@app.callback(
    Output('checklist-plots-scatter', 'figure'),
    Input('checklist-plots-checklist', 'value'))

def update_figure(values):
    fig = px.scatter(
        df[df["species"].isin(values)],
        x="sepal_length",
        y="sepal_width", 
        color="species",
        color_discrete_map=color_discrete_map,
        range_x=range_x,
        range_y=range_y
    )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)