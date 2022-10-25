from dash import Dash, dash_table, dcc, html, Input, Output, State, MATCH, ctx
from dash.dash_table import FormatTemplate
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
    return dash_table.DataTable(
        dff.to_dict("records"),
        [
            {"name": col, "id": col},
            {
                "name": "Sales",
                "id": "sale_dollars",
                "type": "numeric",
                "format": FormatTemplate.money(2),
            },
        ],
        style_cell={"textAlign": "left"},
        style_cell_conditional=[
            {"if": {"column_id": "sale_dollars"}, "textAlign": "right"}
        ],
        style_header={"backgroundColor": "white", "fontWeight": "bold"},
        style_as_list_view=True,
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
        dbc.Button("Add List", id="top10-add-list", n_clicks=0, className="m-3"),
        dbc.Button("Clear", id="top10-clear", className="m-3", outline=True, color="primary"),
        html.Div(id="top10-container", children=[], className="mt-3"),
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
    Output({"type": "top10-table", "index": MATCH}, "data"),
    Output({"type": "top10-table", "index": MATCH}, "columns"),
    Input({"type": "top10-col", "index": MATCH}, "value"),
)
def update_top10_data(col):
    data = make_top10_dff(col)
    cols = [
        {"name": "Top 10", "id": col},
        {
            "name": "Sales",
            "id": "sale_dollars",
            "type": "numeric",
            "format": FormatTemplate.money(2),
        },
    ]
    return data.to_dict("records"), cols


if __name__ == "__main__":
    app.run_server(debug=True)
