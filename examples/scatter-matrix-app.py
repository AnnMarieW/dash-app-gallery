from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

filepath = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"
df = pd.read_csv(filepath)
# fig = px.scatter_matrix(df)
# fig.show()
dimensions_list = df.columns.values

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Scatterplot Matrix of the Correlates of Diabetes",
            style={'textAlign': 'center'}),
    html.Div(
        [html.H3('Choose your dimensions:',
                 style={"paddingLight": "60px"}),
         dcc.Dropdown(
            id='scatter-matrix-app-x-dimension-dropdown',
            options=dimensions_list,
            value=["Outcome", "Glucose", "BMI"],
            multi=True
        )], style={"display": "inline-block", "verticalAlign": "top", "width": "30%", "margin-left": "5em"}),
    dcc.Graph(
        id='scatter-matrix-app-x-graph'
    )
])


@ app.callback(
    Output('scatter-matrix-app-x-graph', 'figure'),
    [Input("scatter-matrix-app-x-dimension-dropdown", "value")])
def update_graph(dimension_choice):
    fig = px.scatter_matrix(df,
                            dimensions=dimension_choice)
    fig.update_layout()
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
