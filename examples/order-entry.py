from dash import Dash, dash_table, html, Input, Output, ctx
import pandas as pd

product_data = {
    "product": ["apples", "bananas", "milk", "eggs", "bread", "cookies"],
    "price": [3.75, 1.65, 1.55, 3.60, 3.00, 3.97],
    "unit": ["kg", "kg", "l", "dz", "ea", "pkg"],
}
new_order_line = {"product": "", "price": 0, "unit": "", "quantity": 0, "total": 0}

df_product = pd.DataFrame(product_data)
df_new_order_line = pd.DataFrame(new_order_line, index=[0])


app = Dash(__name__)

title = html.H4("Order Entry Table", style={"textAlign": "center", "margin": 30})
add_button = html.Button("+", n_clicks=0, id="order-entry-x-add-btn")
total = html.Div(id="order-entry-x-total", style={"textAlign": "right"})

table = dash_table.DataTable(
    id="order-entry-x-table",
    columns=[
        {
            "name": "Product",
            "id": "product",
            "editable": True,
            "presentation": "dropdown",
        },
        {
            "name": "Quantity",
            "id": "quantity",
            "type": "numeric",
            "format": {"specifier": ",.0f"},
            "editable": True,
            "on_change": {"failure": "default"},
            "validation": {"default": 0},
        },
        {"name": "Unit", "id": "unit"},
        {
            "name": "Price",
            "id": "price",
            "type": "numeric",
            "format": {"specifier": "$,.2f"},
        },
        {
            "name": "Total",
            "id": "total",
            "type": "numeric",
            "format": {"specifier": "$,.2f"},
        },
    ],
    data=df_new_order_line.to_dict("records"),
    row_deletable=True,
    dropdown={
        "product": {
            "options": [{"label": i, "value": i} for i in df_product["product"]]
        },
    },
)

app.layout = html.Div([title, add_button, table, total], style={"margin": 30})


@app.callback(
    Output("order-entry-x-table", "data"),
    Output("order-entry-x-total", "children"),
    Input("order-entry-x-add-btn", "n_clicks"),
    Input("order-entry-x-table", "data"),
    prevent_initial_call=True,
)
def add_row(n_clicks, rows):
    df_order = pd.DataFrame(rows)

    # add a new line
    if ctx.triggered_id == "order-entry-x-add-btn":
        df_order = df_order.append(df_new_order_line, ignore_index=True)

    # update the order
    if rows:
        df_merged = pd.merge(df_order, df_product, how="left", on="product")
        df_order.price = df_merged.price_y
        df_order.unit = df_merged.unit_y
        df_order.total = df_order.price * df_order.quantity

    order_total = df_order.total.sum() if rows else 0
    return df_order.to_dict("records"), f"Total   ${order_total:,.2f}"


if __name__ == "__main__":
    app.run_server(debug=True)
