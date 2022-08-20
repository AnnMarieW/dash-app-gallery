hello = """```python
from dash import Dash, dcc, html, Output, Input
import plotly.express as px

df = px.data.tips()
app = Dash(__name__)

radio_b = dcc.RadioItems(df.columns, 'time')
my_graph = dcc.Graph()
app.layout = html.Div([radio_b, my_graph])

@app.callback(Output(my_graph, 'figure'),
              Input(radio_b, 'value'))
def update_graph(value):
   fig = px.bar(df, x=value, y="tip")
   return fig

if __name__ == '__main__':
   app.run()
   
```"""
