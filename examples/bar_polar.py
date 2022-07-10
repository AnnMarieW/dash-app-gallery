from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

filepath = (
    "https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv"
)
df = pd.read_csv(filepath)

state_list = df["state"].unique()

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H2(
            f"Polar Charts of U.S. Agricultural Exports, 2011",
            style={"textAlign": "center"},
        ),
        html.Div("Choose the radius scale:"),
        dcc.RadioItems(
            id="bar-polar-app-x-radio-items",
            options=["Absolute", "Logarithmic"],
            value="Logarithmic",
        ),
        html.Br(),
        html.Div("Choose States:"),
        dcc.Dropdown(
            id="bar-polar-app-x-dropdown",
            value=state_list[:6],
            options=state_list,
            multi=True,
        ),
        dcc.Graph(id="bar-polar-app-x-graph"),
    ],
    style={"margin": "1em 5em", "fontSize": 18},
)


@app.callback(
    Output("bar-polar-app-x-graph", "figure"),
    Input("bar-polar-app-x-dropdown", "value"),
    Input("bar-polar-app-x-radio-items", "value"),
)
def update_graph(state, radius_scale):
    filtered_df = df[df["state"].isin(state)]
    log_r = True if radius_scale == "Logarithmic" else False

    fig = px.bar_polar(
        filtered_df,
        r=filtered_df["total exports"],
        theta=filtered_df["state"],
        color=filtered_df["total exports"],
        template="plotly_white",
        color_continuous_scale=px.colors.sequential.Plasma,
        log_r=log_r,
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
