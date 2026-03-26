# How to contribute your app to this project
 
The Example Index is designed for people new to Dash and/or new to coding.  If you have a beginner-friendly, complete
minimal example of core dash features such as  figures, components, callbacks and layout design we'd love to see it!

Below is a long list of requirements and a detailed code review checklist.  This is necessary for the apps to work when
added to the gallery and to make sure there is a consistent coding style for the entire project. Please review the list
and complete as many as possible, but don't worry about completing everything.  We'll either do the rest together during
the pull request, or we can just make the necessary changes for you.

Thank you for contributing an app to the community supported `Dash Example Index` project!


## Requirements for new apps

- **Content**: Every app should include a graph or a Dash Ag Grid, a callback, and a maximum of 150 lines of code.
- **Uniqueness:** The app should be different from others in the Example Index.
- **Dependencies:** No new dependencies without prior approval.
- **Datasets:** Please try to use  the built-in [Plotly Express datasets](https://plotly.com/python-api-reference/generated/plotly.express.data.html) or the datasets located in [Plotly's repo](https://github.com/plotly/datasets). Other data sets may be used with prior approval.



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




### How to contribute

If you have never contributed to an opens source project, this is a great place to start. Here's how:
1. Open an issue and include your code and an image of the app, and we'll take it from there. (The easiest way)  
2. Or fork the repo and create a pull request. If you are new to creating pull requests, here's a video by Adam on how to [fork a repo and creating a Pull Request](https://youtu.be/Xth83OD3NNc)

### Where to add new apps

To add apps to this project, place your example apps in the `examples/` folder. The most convenient way of doing this is by [forking our repo and creating a Pull Request](https://youtu.be/Xth83OD3NNc) for each app that you would like to add.



### Code Review Checklist

Every app goes through an extensive code review process.  Prior to opening a pull prequest please review this list and complete
as many items as possible.

Basic Requirements
- [ ] App is beginner-friendly and demonstrates  basic dash features with ~150 lines of code or less. Typically includes a figure and/or a table and at least one callback.
- [ ] Code is easy to read, maintain and extend.
- [ ] App is different from others in the Example Index.
- [ ] Runs error free as a stand-alone app in a virtual environment made from the current [`requirements.txt`](https://github.com/AnnMarieW/dash-app-gallery/blob/main/requirements.txt). Adding anything to the `requriements.txt` needs prior approval.
- [ ] Must include  `__name__`  in app instantiation and may include a Bootstrap external stylesheet.  Anything else needs prior approval.
- [ ] Does not include the following since it will not work in production: `app.title = "...."`      `server = app.server`
- [ ] Uses [Plotly built-in datasets](https://plotly.com/python-api-reference/generated/plotly.data.html) or data from https://github.com/plotly/datasets.  Unique data sets may be added temporarily to the [`assets`](https://github.com/AnnMarieW/dash-app-gallery/tree/main/assets) folder for use during review.  Before deployment, the data will be moved to the Plotly datasets repo.
- [ ] Has no errors in the console
- [ ] Code is formatted with black==21.6b0  (same version as used with Dash)
- [ ] Ensure the layout is responsive - ie is functional and looks nice in various browser window sizes
- [ ] Uses minimal styling, so it's easy for people to adapt the app for use in their own projects without removing a lot of custom style.


Naming conventions
- [ ] Uses descriptive variable names
- [ ] Uses python standard snake_case  variable names  ie `submit_button`
- [ ] For `id`'s, uses hyphens.  ie `id="submit-button"`.  Note - In production the ids will have the filename as a prefix (`<filename>-x-`)  See the Unique Ids section below.
- [ ] In the `style` prop, uses camel case: ie `style={"textAlign": "center"}`
- [ ] Uses `df` for main pandas dataframe in the global scope.  Uses `dff` for the filtered `df` in a callback function.


Concise code
- [ ] Uses concise syntax available in Dash>=2.0
For example use `dcc.Dropdown(df.columns)` rather than `dcc.Dropdown(options = [{'label':c, 'value':c} for c in df.columns]`
- [ ] Does not put callback `Input()`s `Output()`s or `State()`s in a list
- [ ] Does not include props that are set to the defaults for the component.  For example,  it's not necessary to include `multi=False` in the `dcc.Dropdown`.  Check the reference section of the docs to see the defaults for the components.
- [ ] Does not include unused imports
- [ ] Uses Minimal comments - only those necessary to describe "why" rather than just describing what the code does.
- [ ] Uses f-strings rather than `.format()`


In apps using `dash-bootstrap-components`:
- [ ] Uses `className` prop whenever possible instead of the  `style` prop. For example:  `className="bg-primary"` rather than `style={"backgroundColor": "blue"}`
- [ ] Uses named Bootstrap colors rather than custom colors wherever possible
- [ ] Avoids using `html.BR()` for spacing and instead uses margin in the `className` prop
- [ ] Uses `dbc.Button` instead of `html.Button`.
- [ ]  Uses `dbc.Container` as the outer container of the app rather than `html.Div`
- [ ] Works well with `dbc.themes.SPACELAB` sine that is the stylesheet used in production.


Before release:  (For Maintainers only)
- [ ] Checklist above is  complete
- [ ]  Ensure IDs are unique by adding prefix `<filename>-x-`
- [ ] Add app image to the `assets` folder
- [ ] Remove any data files added to the `assets` folder during review
- [ ] Add data files to Plotly datasets repo (if any)
- [ ] Include the new app by adding the related file to the `pages` folder and run  `app.py` from the root directory to ensure the new app works in the Example Index.
- [ ] add entry to the CHANGELOG.md
- [ ] Release :party:



### Unique IDs

It's a Dash requirement that every ID in a multi-page app is unique, otherwise the callbacks will not work. To ensure unique IDs,  add `[name-of-the-file]-x-` to every ID. This will ensure that each ID, across the files, is unique.

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
