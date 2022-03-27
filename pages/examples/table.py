from dash import Dash, html, Input, Output, dash_table
import pandas as pd

data_url = (
    "https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv"
)
df = pd.read_csv(data_url)  # replace with your own data source

app = Dash(__name__)


app.layout = html.Div(
    [
        html.H4("Simple interactive table"),
        html.P(id="table-x-table_out"),
        dash_table.DataTable(
            id="table-x-table",
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict("records"),
            style_cell=dict(textAlign="left"),
            style_header=dict(backgroundColor="paleturquoise"),
            style_data=dict(backgroundColor="lavender"),
        ),
    ]
)


@app.callback(
    Output("table-x-table_out", "children"), Input("table-x-table", "active_cell")
)
def update_graphs(active_cell):
    if active_cell:
        cell_data = df.iloc[active_cell["row"]][active_cell["column_id"]]
        return f'Data: "{cell_data}" from table cell: {active_cell}'
    return "Click the table"


if __name__ == "__main__":
    app.run_server(debug=True)
