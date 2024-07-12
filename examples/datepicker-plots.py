import pandas as pd
from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
import time

df = px.data.stocks()
df['date'] = pd.to_datetime(df['date'])
app = Dash(__name__, external_stylesheets=[
    'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css'
])

app.layout = html.Div([
    html.Label('Plot Type', style={'marginBottom': '5px', 'fontWeight': 'bold'}),
    dcc.Dropdown(
        id='datepicker-plots-x-dropdown',
        options=[
            {'label': 'Line Plot', 'value': 'line'},
            {'label': 'Scatter Plot', 'value': 'scatter'},
            {'label': 'Area Plot', 'value': 'area'},
            {'label': 'Correlation Matrix', 'value': 'correlation'}
        ],
        clearable=False,
        value='correlation',
        className='mb-3'
    ),
    html.Div([
        html.Div([
            html.Label('Start Date', style={'marginRight': '10px', 'fontWeight': 'bold'}),
            dcc.DatePickerSingle(
                id='datepicker-plots-x-start-date',
                date=df['date'].min(),
                min_date_allowed=df['date'].min(),
                max_date_allowed=df['date'].max(),
                placeholder='Select a date'
            ),
        ], style={'marginRight': '20px'}),
        html.Div([
            html.Label('End Date', style={'marginRight': '10px', 'fontWeight': 'bold'}),
            dcc.DatePickerSingle(
                id='datepicker-plots-x-end-date',
                date=df['date'].max(),
                min_date_allowed=df['date'].min(),
                max_date_allowed=df['date'].max(),
                placeholder='Select a date'
            ),
        ], style={'marginLeft': '20px'}),
    ], style={'display': 'flex', 'justifyContent': 'space-evenly'}),

    html.Div([
        html.Button('Submit', id='datepicker-plots-x-submit', n_clicks=0, style={'backgroundColor': '#1976D2', 'color': 'white', 'border': 'none', 'padding': '10px 20px','textAlign': 'center', 'textDecoration': 'none', 'display': 'inline-block', 'fontSize': '16px', 'margin': '4px 2px', 'cursor': 'pointer', 'borderRadius': '4px'})
    ], style={'display': 'flex', 'justifyContent': 'center', 'marginTop': '20px'}),
    html.Div(id='datepicker-plots-x-error-msg', style={'color': 'orange', 'marginTop': '20px', 'fontSize': 30, 'textAlign': 'center'}),
    dcc.Loading(
        id="datepicker-plots-x-loading",
        type="circle",
        children=[html.Div(id='datepicker-plots-x-graph', children=[], style={'marginTop': '20px'})],
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
    if not start_date:
        return [], 'Please select a start date!'
    if not end_date:
        return [], 'Please select an end date!'
    if end_date <= start_date:
        return [], 'End date should be greater than start date!'

    mask = (df['date'] >= start_date) & (df['date'] <= end_date)
    filtered_df = df.loc[mask]

    time.sleep(1) #To simulate a longer running callback

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