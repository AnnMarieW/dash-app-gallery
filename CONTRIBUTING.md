# How to contribute an app to the Dash App Gallery 
Thank you for contributing an app to the community supported `dash-app-gallery` project! 
Plese keep in mind that this gallery is designed for people new to Dash and/or new to coding.


## Requirements for new apps

- Every app should have a graph or a Dash DataTable, a callback, and strive to be simple wtih approximately 150 lines of code. 

   <details>
     <summary>Possible Graphs to include:</summary>
    area<br/>
    bar<br/>
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
    histogram<br/>
    icicle<br/>
    line_3d<br/>
    line_geo<br/>
    line_mapbox<br/>
    line_polar<br/>
    line_ternary<br/>
    line<br/>
    parallel_categories<br/>
    parallel_coordinates<br/>
    pie<br/>
    scatter<br/>
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
    clientside callback<br/>
    flexible callback signature<br/>
    general<br/>
    multiple outputs<br/>
    pattern matching<br/>
    callback with ctx<br/>
    randomly generated ID<br/>
    pre-defined ID<br/>
   </details>

   * If you are including a clientside callback, use `dash.clientside_callback` rather than `app.clientside_callback`.

* If your app requires data files, provide a link to the data rather and include it in the assets folder.
This will make it easier for people to simply copy, paste and run the sample apps without having to create
an assets folder locally.

### Unique IDs

The Dash App Gallery creates a multi-page app based on the example apps.  It's a Dash requirement that every
id in a multi-page app is unique otherwise the callbacks will not work.

If you are using [auto generated ids](https://dash.plotly.com/basic-callbacks#passing-components-into-callbacks-instead-of-ids), the id will be unique.  

**However, if you choose to specify the id of each component, make sure to add `[name-of-the-file]-x-` to every id. This will ensure that none of the ids across the files clash.** 

Example for pages/axes.py, where we add `axes-x-` to all ids.
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

If your app name, for example, is box-plots.py, you would add `box-plots-x-` in front of every id. 

### Where to add new apps

To add apps to the gallery, place your example apps in the `examples/` folder.

