import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import time

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
tips = px.data.tips()
iris = px.data.iris()
carshare = px.data.carshare()

app.layout = html.Div([
    html.Label('Dataset', style={'margin-top': '15px', 'margin-bottom': '5px', 'font-weight': 'bold', 'display': 'flex', 'justify-content': 'center'}),
    html.Div([
    dcc.Dropdown(
        id='dataset-dropdown',
        options=[
            {'label': 'Tips', 'value': 'tips'},
            {'label': 'Iris', 'value': 'iris'},
            {'label': 'Carshare', 'value': 'carshare'}
        ],
        placeholder="Select a dataset",
        style={'width': '100%', 'max-width': '600px'}
    ),], style={'display':'flex', 'justify-content': 'center', 'align-items': 'center', 'margin-bottom': '40px', 'margin-top':'10px'}),
    html.Div([
        dbc.Button('Show Pie Chart', id='pie-button', n_clicks=0, color="primary", className="mr-1"),
        dbc.Button('Show Bar Plot', id='histogram-button', n_clicks=0, color="primary", className="mr-1")
    ], style={'display': 'flex', 'justify-content': 'center', 'margin-top': '20px', 'gap': '150px'}),
    html.Div(id='error-message', style={'color': 'red', 'margin-top': '20px', 'text-align': 'center'}),
    dcc.Loading(
        id="loading",
        type="circle",
        children=[html.Div(id='graph-container', children=[], style={'margin-top': '20px'})],
        custom_spinner=html.H2(["Loading in progress...  ", dbc.Spinner(color="primary", id="loading-output")]),
    ),
])

@app.callback(
    Output('graph-container', 'children'),
    Output('loading-output', 'children'),
    Output('error-message', 'children'),
    Input('pie-button', 'n_clicks'),
    Input('histogram-button', 'n_clicks'),
    State('dataset-dropdown', 'value')
)

def update_graph(n_clicks_pie, n_clicks_bar, selected_dataset):
    if n_clicks_pie == 0 and n_clicks_bar == 0:
        return [], '', ''
    
    if not selected_dataset:
        return [], '', 'Please select a dataset!'

    ctx = dash.callback_context
    time.sleep(0.40)
    if not ctx.triggered:
        return [], '', ''
    
    else:
        datasets = {'tips': tips, 'iris': iris, 'carshare': carshare}
        pie_names = {'tips': 'day', 'iris': 'petal_length', 'carshare': 'peak_hour'}
        bar_x_y = {'tips': ('day', 'total_bill'), 'iris': ('species', 'sepal_length'), 'carshare': ('peak_hour', 'car_hours')}

        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == 'pie-button':
            fig = px.pie(datasets[selected_dataset], names=pie_names[selected_dataset])
            fig.update_layout(title_text=f'Pie Chart for {selected_dataset} dataset')
        elif button_id == 'histogram-button':
            x, y = bar_x_y[selected_dataset]
            fig = px.histogram(datasets[selected_dataset], x=x, color=y, nbins=50)
            fig.update_layout(title_text=f'Histogram for {selected_dataset} dataset')
        return dcc.Graph(figure=fig, style={'border': '2px solid black', 'margin':'50px'}), '', ''

if __name__ == '__main__':
    app.run_server(debug=True)