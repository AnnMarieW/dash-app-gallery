from dash import Dash, dcc, html, Input, Output
import pandas as pd
from datetime import date
import plotly.express as px

filepath = "https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv"
df = pd.read_csv(filepath)

state_list = list(df["state"].unique())

chosen_list = ["Alabama", "Alaska", "Arizona"]

app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1(f'Polar Charts of U.S. Agricultural Exports, 2011',
                style={'textAlign': 'center'})]),
    html.Div([
        html.H2('Choose the radius scale (absolute or logarithmic), then choose states:',
                style={"margin-left": "5em"}),
        html.Div(
            [dcc.RadioItems(
                id="bar-polar-app-x-radio-items",
                options=["Absolute", "Logarithmic"],
                value="Absolute"
            )
            ], style={"width": "50%",
                      'font-size': 20,
                      "marginLeft": "6em"}
        ),
        html.Div([html.Br()]),
        html.Div([dcc.Dropdown(
            id='bar-polar-app-x-dropdown',
            value=state_list[:6],
            options=state_list,
            multi=True,
            style={'font-size': 16,
                   "width": "90%",
                   "marginLeft": "3.8em"}
        ),
            dcc.Graph(id='bar-polar-app-x-graph',
                      style={
                          "margin-left": "5em", })

        ], style={"width": "90%"}
        )
    ], style={"width": "100%"}
    )
]
)


@ app.callback(
    Output('bar-polar-app-x-graph', 'figure'),
    [Input("bar-polar-app-x-dropdown", "value"),
     Input("bar-polar-app-x-radio-items", "value")])
def update_graph(state, radius_scale):
    filtered_df = df[df["state"].isin(state)]
    if radius_scale == "Absolute":
        fig = px.bar_polar(filtered_df, r=filtered_df["total exports"], theta=filtered_df["state"],
                           color=filtered_df["total exports"], template="plotly_white",
                           color_continuous_scale=px.colors.sequential.Plasma,
                           log_r=False)
        return fig
    elif radius_scale == "Logarithmic":
        fig = px.bar_polar(filtered_df, r=filtered_df["total exports"], theta=filtered_df["state"],
                           color=filtered_df["total exports"], template="plotly_white",
                           color_continuous_scale=px.colors.sequential.Plasma,
                           log_r=True)
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)
