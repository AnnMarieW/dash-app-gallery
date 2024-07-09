import pandas as pd
from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
import dash_bootstrap_components as dbc
import time

df = px.data.stocks()
df['date'] = pd.to_datetime(df['date'])
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.Label('Plot Type', style={'margin-bottom': '5px', 'font-weight': 'bold'}),
    dcc.Dropdown(
        id='datepicker-plots-x-dropdown',
        options=[
            {'label': 'Select a plot', 'value': ''},
            {'label': 'Line Plot', 'value': 'line'},
            {'label': 'Scatter Plot', 'value': 'scatter'},
            {'label': 'Area Plot', 'value': 'area'},
            {'label': 'Correlation Matrix', 'value': 'correlation'}
        ],
        value='correlation',
        className='mb-3'
    ),
    html.Div([
        html.Div([
            html.Label('Start Date', style={'margin-right': '10px', 'font-weight': 'bold'}),
            dcc.DatePickerSingle(
                id='datepicker-plots-x-start-date',
                date=df['date'].min(),
                min_date_allowed=df['date'].min(),
                max_date_allowed=df['date'].max(),
                placeholder='Select a date'
            ),
        ], style={'margin-right': '20px'}),
        html.Div([
            html.Label('End Date', style={'margin-right': '10px', 'font-weight': 'bold'}),
            dcc.DatePickerSingle(
                id='datepicker-plots-x-end-date',
                date=df['date'].max(),
                min_date_allowed=df['date'].min(),
                max_date_allowed=df['date'].max(),
                placeholder='Select a date'
            ),
        ], style={'margin-left': '20px'}),
    ], style={'display': 'flex', 'justify-content': 'space-evenly'}),

    html.Div([
        dbc.Button('Submit', id='datepicker-plots-x-submit', n_clicks=0, color="primary", className="mr-1")
    ], style={'display': 'flex', 'justify-content': 'center', 'margin-top': '20px'}),
    html.Div(id='datepicker-plots-x-error-msg', style={'color': 'orange', 'margin-top': '20px', 'font-size': 30, 'text-align': 'center'}),
    dcc.Loading(
        id="datepicker-plots-x-loading",
        type="circle",
        children=[html.Div(id='datepicker-plots-x-graph', children=[], style={'margin-top': '20px'})],
    ),
])

@app.callback(
        Output('datepicker-plots-x-graph', 'children'),
        Output('datepicker-plots-x-error-msg', 'children'),
        Input('datepicker-plots-x-submit', 'n_clicks'),
        State('datepicker-plots-x-dropdown', 'value'),
        State('datepicker-plots-x-start-date', 'date'),
        State('datepicker-plots-x-end-date', 'date')
)
def update_graph(n_clicks, plot_type, start_date, end_date):
    if not plot_type:
        return [], 'Please select a plot type!'
    if not start_date:
        return [], 'Please select a start date!'
    if not end_date:
        return [], 'Please select an end date!'
    if end_date <= start_date:
        return [], 'End date should be greater than start date!'

    mask = (df['date'] >= start_date) & (df['date'] <= end_date)
    filtered_df = df.loc[mask]

    time.sleep(0.25)

    plot_funcs = {
        'line': px.line,
        'scatter': px.scatter,
        'area': px.area,
        'correlation': lambda data, x, y: px.imshow(data.corr())
    }

    if plot_type == 'correlation':
        fig = plot_funcs[plot_type](filtered_df.drop('date', axis=1), x=None, y=None)
    else:
        fig = plot_funcs[plot_type](filtered_df, x='date', y=filtered_df.columns.drop('date'))

    return dcc.Graph(figure=fig), ''

if __name__ == '__main__':
    app.run_server(debug=True)