# How to contribute your app to this project 
Thank you for contributing an app to the community supported `Dash Example Index` project! 
Plese keep in mind that this gallery is designed for people new to Dash and/or new to coding, so let's try to keep the code simple.

## Requirements for new apps

Every app should have a graph or a Dash DataTable, a callback, and a maximum of 150 lines of code. 

   <details>
     <summary>Please include any of the following graphs into your app:</summary>
    area<br/>
    bar_polar<br/>
    box plot<br/>
    candlestick<br/>
    choropleth_mapbox<br/>
    choropleth<br/>
    contour<br/>
    density_contour<br/>
    density_heatmap<br/>
    density_mapbox<br/>
    ecdf<br/>
    funnel_area<br/>
    funnel<br/>
    icicle<br/>
    line_3d<br/>
    line_geo<br/>
    line_mapbox<br/>
    line_polar<br/>
    line_ternary<br/>
    parallel_categories<br/>
    parallel_coordinates<br/>
    pie<br/>
    scatter_3d<br/>
    scatter_geo<br/>
    scatter_mapbox<br/>
    scatter_matrix<br/>
    scatter_polar<br/>
    scatter_ternary<br/>
    strip<br/>
    sunburst<br/>
    timeline<br/>
    treemap<br/>
    violin<br/>
   </details>

   <details>
     <summary>Possible callbacks to include:</summary>
    chained<br/>
    circular callback<br/>
    clientside callback (use dash.clientside_callback rather than app.clientside_callback)<br/>
    flexible callback signature<br/>
    pattern matching<br/>
    callback context (ctx)<br/>
    regular callback
   </details>

### Data
For incorporating data into your app, please try to use the built-in [Plotly Express datasets](https://plotly.com/python-api-reference/generated/plotly.express.data.html) or the datasets located in [Plotly's repo](https://github.com/plotly/datasets). 

### Unique IDs

It's a Dash requirement that every ID in a multi-page app is unique, otherwise the callbacks will not work. To ensure unique IDs, please use either method A or B. 

A. You can safely use [auto generated ids](https://dash.plotly.com/basic-callbacks#passing-components-into-callbacks-instead-of-ids). 

B. **However, if you choose to specify the ID of each component, make sure to add `[name-of-the-file]-x-` to every ID. This will ensure that each ID, across the files, is unique.** 

For example, if you look at the [axes.py file in the examples folder](https://github.com/AnnMarieW/dash-app-gallery/blob/main/examples/axes.py), you will see that we added a `axes-x-` to all IDs (because the name of the file is axes.
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
After the Dash is built, `axes-x-` is removed and the code that is displayed to the user will look like:
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

If your app name, for example, is box-plots.py, you would add `box-plots-x-` in front of every id. 

### Where to add new apps

To add apps to this project, place your example apps in the `examples/` folder. The most convenient way of doing this is by [forking our repo and creating a Pull Request](https://youtu.be/Xth83OD3NNc) for each app that you would like to add. 

