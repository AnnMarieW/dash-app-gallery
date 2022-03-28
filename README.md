# Instructions

This app creates gallery of example apps using `pages/` the Multi-page app plug-in from dash-labs.  

For more information on `paages/` see the forum post https://community.plotly.com/t/introducing-dash-pages-a-dash-2-x-feature-preview
Or the live demo : https://dashlabs.pythonanywhere.com/

## Running the app

After cloning the repo, run `app.py`



## Adding Examples

### Example app source code

To add apps to the gallery, place dash example apps in the `pages/examples/` folder.

### App Image

Add an image of the app in the `assets/` folder.  Make the image filename the same name as the source
code filename.  For example, if the file name is `3d-scatter-plots.py`, then the image filename
should be `3d-scatter-plots.pgn`  (or whatever image file extension you are using)

The `pages/` plugin will automatically use this image to create the meta tags.  This image will also be used in the 
card grid on the home page.  If no image is provided, then it will default to  `app.pgn` .

### Unique IDs
If you are creating/adjusting examples, you need to make sure that every id is unique otherwise the callbacks will not work.

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

## Registering the page and creating the page layout

Each page of the multi-page app is defined by a file in the root of the `pages/` folder

Here is an example of `colorscales.py:

```python
import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Dash Sample App")


def layout():
    return example_app(f"pages/examples/colorscales.py")

```

## Changing the app design

### App frame:  `app.py`

The app.py file defines the "app frame".  Here you can define the the parts of the app
that remain constant across all pages, such as the header, footer, main naviation,  `dcc.Store`
components etc. 

### App Gallery Home page

The home page is a grid of cards with a preview of each example app.  You can see two sample designs in
- `pages/home`  - grid only
- `pages/home-search` - grid with some dropdowns to select apps by category

To select apps by category, extra data can be added to `dash.page_registry` for each app. This can be
used to select apps in dropdowns or search fields.  See an example of this in the following files:
- `pages/3d-scatter-plots.py`
- `pages/exmaples3d-scatter-plots.py`
- `pages/home-search.py`

![image](https://user-images.githubusercontent.com/72614349/160307582-feaf3568-30a1-47f5-a464-5f9886b0d0ca.png)

### Code and Show pages

Once you select an app, it will show the app and/or the code

The layout for the app is defined in the `example_app()` function which you can find in `utils/code_and_show.py`.

```
def example_app(filename, make_layout=None, run=True, show_code=True):
```
    
Creates the "code and show" layout for an example dash app.

- `filename`:
   The path to the file with the sample app code.  


- `make_layout`:
    A function which takes as attributes the code string and the live app and returns a
    layout.  The default layout displays the code side-by-side with the live app on large screens
    or app first followed by the code on smaller screens.  

    
- `run`:
    bool (default: True) Whether to run the app.  

    
- `show_code`:
    bool (default: True) Whether to show the code   


![image](https://user-images.githubusercontent.com/72614349/160307783-af71ae67-4672-4ee8-a0d2-e06d9dd71510.png)


### Create custom code and show layouts

You can pass your own function to `example_app()` to customize the layout.

For example, this layout will show the app first followed by the code on all screen sized:

```python

def make_app_first(code, show_app):
    """
    This is an alternate layout for the "code and show"
    It displays the app on top and the code below.
    This function can be used as an example of how to create your own custom layouts
    to be used with example_app() .

    Use this layout instead of the default by passing this function
    to the `make_layout` attribute in example_app()   e.g.:
    `example_app("pathto/my_filename.py", make_layout=make_app_first)`
    """
    code = dcc.Markdown(f"```python\n{code}```\n")
    return dbc.Row(
        [
            dbc.Col(dbc.Card(show_app, style={"padding": "10px"}), width=12)
            if show_app
            else None,
            dbc.Col(
                dbc.Card([code], style={"max-height": "500px", "overflow": "auto"}),
                width=12,
            )
            if code
            else None,
        ]
    )

```

