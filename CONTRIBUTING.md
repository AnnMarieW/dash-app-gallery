# How to contribute an app to the Dash App Gallery 


## Running the app

After cloning the repo, run `app.py`



## Adding Examples

Thank you for contributing an app to the community supported `dash-app-gallery` project!


Please keep in mind that this gallery is designed for people new to Dash and/or new to coding. Please keep
the examples simple and approximately 150 lines of code.

If you are including a clientside callback, use `dash.clientside_callback` rather than `app.clientside_callback`
(This is a bug which we hope to fix soon)

If your app requires data files, provide a link to the data rather and include it in the assets folder.
This will make it easier for people to simply copy, paste and run the sample apps without having to create
an assets folder locally.


### Example app source code

To add apps to the gallery, place dash example apps in the `examples/` folder.

### Unique IDs

The Dash App Gallery is creates a multi-page app based on the example apps.  It's a Dash requirement that every
id in a multi-page app is unique otherwise the callbacks will not work.

To do this, add `[name-of-the-file]-x-` to every id. This will ensure that none of the ids across the files clash. 

This extra bit is then automatically removed from the displayed code, such that it remains simple and readable.

Example for pages/axes.py, where we add `axes-x-` to all id.
```
app.layout = html.Div([
    html.H4('Interactive Plotly Express axes'),
    html.Button("Rotate labels", n_clicks=0, 
                id='axes-x-button'),
    dcc.Graph(id="axes-x-graph"),
])


@app.callback(
    Output("axes-x-graph", "figure"), 
    Input("axes-x-button", "n_clicks"))
def rotate_figure(n_clicks):
    df = px.data.tips() # replace with your own data source
    fig = px.histogram(df, x="sex", height=500)
    fig.update_xaxes(tickangle=n_clicks*45)
    return fig
```
After the Dash is built, `axes-x-` is removed and the code that is displayed will looks like:
```
app.layout = html.Div([
    html.H4('Interactive Plotly Express axes'),
    html.Button("Rotate labels", n_clicks=0, 
                id='button'),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    Input("button", "n_clicks"))
def rotate_figure(n_clicks):
    df = px.data.tips() # replace with your own data source
    fig = px.histogram(df, x="sex", height=500)
    fig.update_xaxes(tickangle=n_clicks*45)
    return fig
```

For pages/box-plots.py we  would add `box-plots-x-` in front of every id. 
