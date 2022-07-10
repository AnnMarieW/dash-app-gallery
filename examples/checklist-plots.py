import plotly.express as px
from dash import Dash, dcc, html, Output, Input
from plotly import data

df = data.iris()

species = df["species"].unique().tolist()

options = [{"label": specie.capitalize(), "value": specie} for specie in species]

app = Dash(__name__)

app.layout = html.Div(
    [
        dcc.Checklist(
            options=options,
            inline=True,
            value=species,
            id="checklist-plots-x-checklist",
        ),
        dcc.Graph(id="checklist-plots-x-scatter"),
    ]
)


@app.callback(
    Output("checklist-plots-x-scatter", "figure"),
    Input("checklist-plots-x-checklist", "value"),
)
def update_figure(values):
    fig = px.scatter(
        df[df["species"].isin(values)],
        x="sepal_length",
        y="sepal_width",
        color="species",
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
