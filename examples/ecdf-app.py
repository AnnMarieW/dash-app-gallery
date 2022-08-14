from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

filepath = "https://raw.githubusercontent.com/plotly/datasets/master/mtl2013ternary.csv"
df = pd.read_csv(filepath)

df["Coderre_pct"] = round(df["Coderre"] / df["total"] * 100, 2)
df["Joly_pct"] = round(df["Joly"] / df["total"] * 100, 2)
df["Bergeron_pct"] = round(df["Bergeron"] / df["total"] * 100, 2)

candidate_list = ["Coderre_pct", "Joly_pct", "Bergeron_pct"]

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1(
            "ECDF of Vote Share (%) by District in Montreal's Municipal Elections, 2013",
            style={"textAlign": "center"},
        ),
        html.Div(
            [
                html.H3("Choose a candidate:"),
                dcc.Dropdown(
                    id="ecdf-app-x-candidate-dropdown",
                    value="Joly_pct",
                    options=candidate_list,
                    multi=True,
                ),
            ],
            style={
                "width": "50%",
                "marginLeft": "5em",
            },
        ),
        dcc.Graph(id="ecdf-app-x-graph"),
    ]
)


@app.callback(
    Output("ecdf-app-x-graph", "figure"),
    Input("ecdf-app-x-candidate-dropdown", "value"),
)
def update_graph(candidate):
    fig = px.ecdf(df, x=candidate)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
