# Instructions

This app creates gallery of example apps using `pages/` the Multi-page app plug-in from dash-labs.  

For more information on `pages/` see the forum post https://community.plotly.com/t/introducing-dash-pages-a-dash-2-x-feature-preview
Or the live demo : https://dashlabs.pythonanywhere.com/

## Running the app

After cloning the repo, run `app.py`



## Adding Examples

### Example app source code

To add apps to the gallery, place dash example apps in the `examples/` folder.

### App Image


The `pages/` plugin will automatically use the app's image in the assets folder to create the meta tags.  This image will also be used in the 
card grid on the home page.  If no image is provided, then it will default to  `app.png` .


`utils_make_images` 
This directory contains the utilities to create the images of a uniform size and shape so they will display nicely in the app gallery overview.
(more info/directions coming soon)


## Changing the app design

### App frame:  `app.py`

The app.py file defines the "app frame".  Here you can define the parts of the app
that remain constant across all pages, such as the header, footer, main navigation,  `dcc.Store`
components etc. 

### App Gallery Home page

The home page is a grid of cards with a preview of each example app.  You can see two sample designs in
- `pages/home-search` - grid with search field and some dropdowns to select apps by category

To select apps by category, extra data can be added to `dash.page_registry` for each app. This can be
used to select apps in dropdowns or search fields.  See an example of this in the following files:
- `pages/3d-scatter-plots.py`
- `pages/exmaples3d-scatter-plots.py`
- `pages/home-search.py`

![image](https://user-images.githubusercontent.com/72614349/160702790-fa1bf95a-abc8-43cd-88aa-a7a7eef65fcf.png)

### Code and Show pages

Once you select an app, it will show the app and/or the code

The layout for the app is defined in the `example_app()` function which you can find in `utils/code_and_show.py`.

Use it to create the layout, for example:

```python
# default side by side layout
code_n_show =  example_app(f"pages/examples/colorscales.py")

# define a function to display a custom layout (see more info below:
code_n_show =  example_app(f"pages/examples/colorscales.py", make_layout=my_custom_layout_function)

code_only = example_app(f"pages/examples/colorscales.py", run=False)

app_only = example_app(f"pages/examples/colorscales.py", show_code=False)


```

Here is more info on `example_app()`

```
def example_app(filename, make_layout=None, run=True, show_code=True, notes=None):
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

- `notes`:
     str (default: None)  Notes or tutorial to display with the app.  Text may include Markdown formatting as it will be displayed in a dcc.Markdown component

![image](https://user-images.githubusercontent.com/72614349/160705938-da83452b-dce2-4236-a658-2e6fcbf8b451.png)


### Create custom code and show layouts

You can pass your own function to `example_app()` to customize the layout.

For example, this layout will show the app first followed by the code on all screen sized:

```python

def make_app_first(code, show_app, notes):
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

