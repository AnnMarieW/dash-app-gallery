from dash import Dash,  dcc, html, Input, Output, State, MATCH, ctx
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/liquor_iowa_2021.csv"
)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

options = [
    "city",
    "county",
    "zip_code",
    "category_name",
    "vendor_name",
    "store_name",
    "item_description",
    "date",
    "invoice_and_item_number",
]


def make_top10_dff(col):
    dff = df[[col, "sale_dollars"]]
    dff = (
        dff.groupby(col)
        .sum()
        .sort_values(by="sale_dollars", ascending=False)
        .head(10)
        .reset_index()
    )
    dff.loc["Total"] = dff.sum(numeric_only=True)
    return dff


def make_table(id, col):
    dff = make_top10_dff(col)
    return dag.AgGrid(
        rowData=dff.to_dict("records"),
        columnDefs =  [
            {"field": col},
            {
                "headerName": "Sales",
                "field": "sale_dollars",
                "valueFormatter":{"function": "d3.format('$,.2')(params.value)"},
                "type":"rightAligned"
            },
        ],
        defaultColDef={"resizable":True},
        style={"height":500},
        id={"type": "top10-table", "index": id},
    )


def make_card(n_clicks, col):
    return dbc.Card(
        [
            dcc.Dropdown(
                options,
                col,
                id={"type": "top10-col", "index": n_clicks},
                clearable=False,
                className="my-4",
            ),
            make_table(n_clicks, col),
        ],
        style={"width": 500, "display": "inline-block"},
        className="m-3 px-2",
    )


app.layout = dbc.Container(
    [
        html.H3("Iowa Liquor Sales 2021 Top 10 Lists", className="ms-3"),
        dbc.Button("Add List", id="top10-add-list", n_clicks=0, className="ms-3"),
        dbc.Button("Clear", id="top10-clear", className="ms-1", outline=True, color="primary"),
        html.Div(id="top10-container", children=[], className="mt-1"),
    ],
    fluid=True,
)


@app.callback(
    Output("top10-container", "children"),
    Input("top10-add-list", "n_clicks"),
    Input("top10-clear", "n_clicks"),
    State("top10-container", "children"),
)
def add_top10_card(n_clicks, _, cards):
    if ctx.triggered_id == "top10-clear":
        return []
    new_card = make_card(n_clicks, options[0])
    cards.append(new_card)
    return cards


@app.callback(
    Output({"type": "top10-table", "index": MATCH}, "rowData"),
    Output({"type": "top10-table", "index": MATCH}, "columnDefs"),
    Output({"type": "top10-table", "index": MATCH}, "columnState"),
    Input({"type": "top10-col", "index": MATCH}, "value"),
)
def update_top10_data(col):
    data = make_top10_dff(col)
    cols = [
        {"headerName": "Top 10", "field": col},
        {
            "headerName": "Sales",
            "field": "sale_dollars",
            "type": "rightAligned",
            "valueFormatter": {"function": "d3.format('($,.2f')(params.value)"},

        },
    ]
    return data.to_dict("records"), cols, [{}]


if __name__ == "__main__":
    app.run_server(debug=True)
