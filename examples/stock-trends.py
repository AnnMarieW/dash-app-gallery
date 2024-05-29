from datetime import date
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import plotly.data as data
import pandas as pd

# Load the stocks data
df = data.stocks()
df['date'] = pd.to_datetime(df['date'])

# Initialize the Dash app
app = Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1('Stock Trends'),
    dcc.DatePickerRange(
        id='stock-trends-date-picker-range',
        min_date_allowed=date(2018, 1, 1),
        max_date_allowed=date(2019, 12, 30),
        start_date=date(2018, 1, 1),
        end_date=date(2019, 12, 30)
    ),
    dcc.Dropdown(
        options=[
            {'label': 'GOOG', 'value': 'GOOG'},
            {'label': 'AAPL', 'value': 'AAPL'},
            {'label': 'AMZN', 'value': 'AMZN'},
            {'label': 'FB', 'value': 'FB'},
            {'label': 'NFLX', 'value': 'NFLX'},
            {'label': 'MSFT', 'value': 'MSFT'}
        ],
        value=['GOOG'],  # Default value
        multi=True,
        id='stock-trends-column-options'
    ),
    dcc.Graph(id='stock-trends-line-chart')
])

# Define the callback to update the line chart based on selected date range and stocks
@callback(
    Output(component_id='stock-trends-line-chart', component_property='figure'),
    Input(component_id='stock-trends-date-picker-range', component_property='start_date'),
    Input(component_id='stock-trends-date-picker-range', component_property='end_date'),
    Input(component_id='stock-trends-column-options', component_property='value')
)
def update_output(start_date, end_date, tickers):

    # Filter the DataFrame based on the selected date range
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

    # Create the line chart
    fig = px.line(filtered_df, x='date', y=tickers, title='Stock Prices Over Time')
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Index',
        legend_title='Stock'
    )
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

