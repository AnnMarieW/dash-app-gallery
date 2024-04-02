from dash import Dash, dcc, Input, Output, Patch, html
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
dims = ["sepal_width", "sepal_length", "petal_width", "petal_length"]
df = px.data.iris()
fig = px.parallel_coordinates(
    df,
    color="species_id",
    dimensions=dims,
    color_continuous_scale=px.colors.diverging.Tealrose,
    color_continuous_midpoint=2,
)

app.layout = dbc.Container(
    [
        html.H4("Filtering Dash AG Grid with Parallel Coordinates"),
        dcc.Graph(id="parallel-coord-filter-x-my-graph", figure=fig),
        dag.AgGrid(
            id="parallel-coord-filter-x-table",
            columnDefs=[{"field": i} for i in df.columns],
            columnSize="sizeToFit",
            defaultColDef={"minWidth":120}
        ),
        dcc.Store(id="parallel-coord-filter-x-activefilters", data={}),
    ]
)


@app.callback(
    Output("parallel-coord-filter-x-table", "rowData"),
    Input("parallel-coord-filter-x-activefilters", "data"),
)
def udpate_table(data):
    if data:
        dff = df.copy()
        for col in data:
            if data[col]:
                rng = data[col][0]
                if isinstance(rng[0], list):
                    # if multiple choices combine df
                    dff3 = pd.DataFrame(columns=df.columns)
                    for i in rng:
                        dff2 = dff[dff[col].between(i[0], i[1])]
                        dff3 = pd.concat([dff3, dff2])
                    dff = dff3
                else:
                    # if one choice
                    dff = dff[dff[col].between(rng[0], rng[1])]
        return dff.to_dict("records")
    return df.to_dict("records")


@app.callback(
    Output("parallel-coord-filter-x-activefilters", "data"),
    Input("parallel-coord-filter-x-my-graph", "restyleData"),
)
def updateFilters(data):
    if data:
        key = list(data[0].keys())[0]
        col = dims[int(key.split("[")[1].split("]")[0])]
        newData = Patch()
        newData[col] = data[0][key]
        return newData
    return {}


if __name__ == "__main__":
    app.run_server(debug=True)
