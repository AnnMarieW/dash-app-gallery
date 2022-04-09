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
        label="Default",
        value=6
    ),
    dcc.Input(
        id="stopwatch-input",
        type="number",
        placeholder="input type integer",
        ),
    daq.PowerButton(
        id='stopwatch-start',
        on=False,
        color='#FF5E5E',
        theme ="dark"
    ),

    # dcc.Slider(
    #     id='stopwatch-x',
    #     min=0,
    #     max=10,
    #     step=1,
    #     value=5
    # ),
])

@app.callback(
    Output('stopwatch-y', 'value'),
    Input('stopwatch-input', 'value'),
    Input("stopwatch-start", 'value')
)
def update_output(value, start_watch):
    value = int(value)
    if start_watch:
        while value > 0 : 
            value-= 1 
            time.sleep(100)
            return str(value)
           
        
    return str(value)

# @app.callback(
#     Output('stopwatch-y', 'value'),
#     Input('stopwatch-start', 'value')
# )
# def update_time(value):
#     return str(value)

if __name__ == '__main__':
    app.run_server(debug=True)