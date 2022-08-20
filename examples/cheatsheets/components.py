common = """```python
html.Button('Submit', n_clicks=0)

dcc.Dropdown(['kiwi', 'banana', 'apple'], value='orange')

dcc.Slider(0,20,5, value=10)
dcc.RangeSlider(0,20,1, value=[5, 15])

dcc.RadioItems(['Purple', 'Red','Pink'], value='Red')

dcc.Markdown("# This is a heading")

dcc.Textarea(      
value='Textarea content',
style={'width': '100%',  'height': 300})

dcc.Input()

df = px.data.tips()
fig = px.bar(df, x='time',y='tip')
dcc.Graph(figure=fig)

dash_table.DataTable(
    data.to_dict("records"),
    [{"name": i, "id": i} for i in data.columns],
    page_size=10,
    style_table={"overflow-x": "auto"},
)
```"""
