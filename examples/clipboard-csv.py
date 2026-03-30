from dash import Dash, dcc, html, Input, Output, State
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px

app = Dash()

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/mtcars.csv")

app.layout = html.Div(
    [
        html.H2("CSV Clipboard Example"),
        html.P(
            "Copy mtcars.csv by clicking on the clipboard below. Paste the copied content into a notepad or Excel sheet to see the result."
        ),
        dcc.Clipboard(id="clipboard-csv-x-clip", style={"fontSize": 20}),
        dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=[{"field": i} for i in df.columns],
            id="clipboard-csv-x-table",
        ),
        dcc.Graph(id="clipboard-csv-x-graph"),
        html.P("Select x variable:", style={"textAlign": "center"}),
        dcc.RadioItems(
            id="clipboard-csv-x-selection",
            options=["disp", "hp", "drat", "wt", "qsec"],
            value="hp",
            style={"textAlign": "center"},
            inline=True,
        ),
    ]
)


@app.callback(
    Output("clipboard-csv-x-clip", "content"),
    Input("clipboard-csv-x-clip", "n_clicks"),
    State("clipboard-csv-x-table", "rowData"),
)
def custom_copy(_, data):
    dff = pd.DataFrame(data)
    # See options for .to_csv() or .to_excel() or .to_string() in the  pandas documentation
    return dff.to_csv(index=False)  # includes headers


@app.callback(
    Output("clipboard-csv-x-graph", "figure"),
    Input("clipboard-csv-x-selection", "value"),
)
def update_graph(col_chosen):
    fig = px.scatter(
        df,
        x=col_chosen,
        y="mpg",
        labels={
            "disp": "Displacement (cu.in.)",
            "hp": "Horsepower",
            "drat": "Rear axle ratio",
            "wt": "Weight (lb/1000)",
            "qsec": "1/4 mile time (seconds)",
            "mpg": "Miles per Gallon",
        },
        title="Interactive Scatter Plot",
        height=500,
    )
    fig.update(layout=dict(title=dict(x=0.5)))  # center title
    return fig


if __name__ == "__main__":
    app.run(debug=True)
