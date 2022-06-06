from dash import Dash, html, dcc, dash_table, Output, Input, State
from dash.exceptions import PreventUpdate
import plotly.express as px

app = Dash(__name__)

df = px.data.iris()
fig = px.parallel_coordinates(
    df,
    color="species_id",
    labels={
        "species_id": "Species",
        "sepal_width": "Sepal Width",
        "sepal_length": "Sepal Length",
        "petal_width": "Petal Width",
        "petal_length": "Petal Length",
    },
    color_continuous_scale=px.colors.diverging.Tealrose,
    color_continuous_midpoint=2,
)

my_graph = dcc.Graph(id="parallel-coord-x-graph", figure=fig)
my_table = dash_table.DataTable(
    data=df.to_dict("records"),
    row_selectable="single",
    page_size=5,
    id="parallel-coord-x-table",
)

app.layout = html.Div([my_graph, my_table])


@app.callback(
    Output("parallel-coord-x-graph", "figure"),
    Input("parallel-coord-x-table", "selected_rows"),
    State("parallel-coord-x-graph", "figure"),
)
def pick(r, f):
    if r is None:
        raise PreventUpdate

    row = (
        df[["sepal_length", "sepal_width", "petal_length", "petal_width", "species_id"]]
        .loc[r[0]]
        .to_list()
    )

    fig = px.parallel_coordinates(
        df,
        color="species_id",
        labels={
            "species_id": "Species",
            "sepal_width": "Sepal Width",
            "sepal_length": "Sepal Length",
            "petal_width": "Petal Width",
            "petal_length": "Petal Length",
        },
        color_continuous_scale=px.colors.diverging.Tealrose,
        color_continuous_midpoint=2,
    )

    # Use `constraintrange` to filter a certain trace. Read more in docs:
    # https://plotly.com/python/reference/parcoords/#parcoords-dimensions

    fig.update_traces(
        dimensions=list(
            [
                dict(constraintrange=[row[0] - row[0] / 100000, row[0]]),
                dict(constraintrange=[row[1] - row[1] / 100000, row[1]]),
                dict(constraintrange=[row[2] - row[2] / 100000, row[2]]),
                dict(constraintrange=[row[3] - row[3] / 100000, row[3]]),
                dict(constraintrange=[row[4] - row[4] / 100000, row[4]]),
            ]
        )
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
