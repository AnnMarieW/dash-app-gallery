import dash
from dash.dependencies import Input, Output
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
import time 

app = dash.Dash(__name__)

app.layout = html.Div([
    
    daq.LEDDisplay(
        id='stopwatch-y',
        label="Stopwatch",
        value=6
    ),
 
    html.Center( 
        [
            html.Header("Enter seconds"),
            dcc.Input(
            id="stopwatch-input",
            type="number",
            placeholder="enter number of seconds here",
            )
        ]
        ),
   
    dcc.Interval(id='trigger-while-button-on',
                 interval=1*1000,
                 n_intervals=0),
    daq.PowerButton(
        id='stopwatch-start',
        on=False,
        color='#FF5E5E',
        theme ="dark"
    ),

])


@app.callback(
    Output('stopwatch-y', 'value'),
    Input('trigger-while-button-on', 'n_intervals'),
    Input('stopwatch-input', 'value'),
    Input("stopwatch-start", 'on'),
    Input('stopwatch-y', 'value'),
)
def update_output(n, input_value, start_watch, led_value):
    
    if input_value != None and start_watch == False: 
        return int(input_value)
    if n > 0 and start_watch == True:
        if led_value > 0:
            led_value -= 1
            return led_value
    return led_value

if __name__ == '__main__':
    app.run_server(debug=True)