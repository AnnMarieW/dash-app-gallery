declared_id = """```python
app.layout = html.Div([
   dcc.Input(id='my-input',
             value='initial value'),
   html.Div(id='my-output')
])

@app.callback(
   Output('my-output','children'),
   Input('my-input', 'value')
)
def update_output(input_value):
   return input_value
```"""

generated_id = """```python
text = dcc.Input(value='hello')
user_input= html.Div()
app.layout = html.Div([
   text, user_input
])

@app.callback(
   Output(user_input,'children'),
   Input(text, 'value')
)
def update_output(input_value):
   return input_value
```"""

multiple = """```python
app.layout = html.Div([
   dcc.Input(id='my-input',
             value='hello'),
   dcc.Slider(0,20,5, value=10,
              id='slider'),
   html.Div(id='my-output1'),
   html.Div(id='my-output2')
])
@app.callback(
   Output('my-output1','children'),
   Output('my-output2','children'),
   Input('slider','value'),
   Input('my-input','value')
)
def update_out(slider,input_v):
   return input_v, str(slider)
```"""

ctx = """```
from dash import Input, Output, callback, ctx

@callback(
    Output("graph", "figure"),
    Input("btn-bar", "n_clicks"),   
    Input("btn-area", "n_clicks"),
)
def display(*_):
    if ctx.triggered_id == "btn-bar":
        return px.bar(dff, x="year", y="pop")
    return px.area(dff, x="year", y="pop")
```"""