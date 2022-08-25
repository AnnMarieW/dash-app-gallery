
from dash import Dash, html, dcc, Input, Output
from dash.dash_table import FormatTemplate, DataTable
from dash.dash_table.Format import Group, Scheme, Symbol, Format
import pandas as pd

app = Dash(__name__)

df = pd.DataFrame(
    {
        "Exchange": ["Canadian Dollar", "Euro", "Japanese Yen", "US Dollar"],
        "CAD": [1, 0.64, 78.91, 75],
        "EUR": [1.56, 1, 122.9, 1.17],
        "JPY": [0.013, 0.0081, 1, 0.0095],
        "USD": [1.33, 0.85, 104.96, 1],
    }
)
df = df.set_index("Exchange")

app.layout = html.Div(
    [
        html.H4("Currency Exchange Table", style={"textAlign": "center", "margin": 30}),
        html.Div(
            [
                "Enter Amount to Exchange",
                dcc.Input(id="currency-exchange-x-input", type="number", value=100),
            ],
            style={"width": 250},
        ),
        html.Div(
            DataTable(
                id="currency-exchange-x-table",
                columns=[
                    {"name": "Currency Exchange Table", "id": "Exchange"},
                    {
                        "name": "Canadian Dollar",
                        "id": "CAD",
                        "type": "numeric",
                        "format": Format()  # formatted using the Format() object
                        .scheme(Scheme.fixed)
                        .precision(2)
                        .symbol_prefix("$")
                        .symbol(Symbol.yes)
                        .symbol_suffix(" CAD")
                        .group(Group.yes),
                    },
                    {
                        "name": "Euro",
                        "id": "EUR",
                        "type": "numeric",
                        "format": {  # formatted "manually"
                            "specifier": "$,.2f",
                            "locale": {
                                "symbol": ["€", " EUR"],
                                "group": ".",
                                "decimal": ",",
                            },
                        },
                    },
                    {
                        "name": "Japanese Yen",
                        "id": "JPY",
                        "type": "numeric",
                        "format": {  # formatted "manually"
                            "specifier": "$,.0f",
                            "locale": {"symbol": ["¥", " JPX"]},
                        },
                    },
                    {
                        "name": "US Dollar",
                        "id": "USD",
                        "type": "numeric",
                        # formatted using FormatTemplate:
                        "format": FormatTemplate.money(2),
                    },
                ],
                data=df.to_dict("records"),
                style_table={"overflowX": "auto"},

            )
        ),
    ], style={"margin": 10}
)


@app.callback(
    Output("currency-exchange-x-table", "data"), Input("currency-exchange-x-input", "value")
)
def update_table(amount):
    dff = df.multiply(amount, fill_value=0) if amount else df.copy()
    return dff.reset_index().to_dict("records")


if __name__ == "__main__":
    app.run_server(debug=True)