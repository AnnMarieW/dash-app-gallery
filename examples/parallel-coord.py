from dash import Dash, html, dcc, Output, Input
import dash_ag_grid as dag
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

my_grid = dag.AgGrid(
    id="parallel-coord-x-table",
    columnDefs=[{"field": i} for i in df.columns],
    rowData=df.to_dict("records"),
    columnSize="sizeToFit",
    defaultColDef={"minWidth": 120, "sortable":True},
    dashGridOptions={"rowSelection": "single"},
)

app.layout = html.Div([my_graph, my_grid])


@app.callback(
    Output("parallel-coord-x-graph", "figure"),
    Input("parallel-coord-x-table", "selectedRows"),
)
def pick(row):
    if row is None:
        raise PreventUpdate

    row = row[0]
    dimensions = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "species_id",
    ]

    # Use `constraintrange` to filter a certain trace. Read more in docs:
    # https://plotly.com/python/reference/parcoords/#parcoords-dimensions

    fig.update_traces(
        dimensions=[
            dict(constraintrange=[row[d] - row[d] / 100000, row[d]]) for d in dimensions
        ]
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
