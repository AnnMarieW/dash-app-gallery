from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

lst = [
    ["North", "Jan", 500],
    ["North", "Feb", 1500],
    ["North", "Mar", 2000],
    ["North", "Apr", 2500],
    ["North", "May", 3000],
    ["East", "Jan", 3000],
    ["East", "Feb", 2000],
    ["East", "Mar", 1000],
    ["East", "Apr", 4000],
    ["East", "May", 4500],
    ["West", "Jan", 1200],
    ["West", "Feb", 1400],
    ["West", "Mar", 1600],
    ["West", "Apr", 1800],
    ["West", "May", 2200],
    ["South", "Jan", 700],
    ["South", "Feb", 900],
    ["South", "Mar", 400],
    ["South", "Apr", 600],
    ["South", "May", 800],
]
df = pd.DataFrame(lst, columns=["Region", "Month", "Salary"])

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

dropdown_menu = dcc.Dropdown(
    id="salaries-by-region-x-dropdown",
    options=["North", "East", "West", "South"],
    value=["North", "East", "West", "South"],
    multi=True,
)

app.layout = dbc.Container(
    [
        html.H2("Salary changes by region"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(dropdown_menu, sm=6, style={"color": "black"}),
                dbc.Col(dcc.Graph(id="salaries-by-region-x-graph"), sm=6),
            ]
        ),
    ]
)


@app.callback(
    Output("salaries-by-region-x-graph", "figure"),
    Input("salaries-by-region-x-dropdown", "value"),
)
def make_line_graph(region_list):
    dff = df[df["Region"].isin(region_list)]
    fig = px.line_3d(dff, x="Region", y="Month", z="Salary", color="Region")
    fig.update_traces(line_width=13)
    fig.update_layout(
        plot_bgcolor="#222222", paper_bgcolor="#222222", font_color="white"
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
