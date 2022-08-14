# Maintainers' Contributing Guide



This document is an overview of the app structure to help guide maintainers of this project.  If you would just like to 
add an example app, please see  [CONTRIBUTING.md](https://github.com/AnnMarieW/dash-app-gallery/blob/main/CONTRIBUTING.md)



The purpose of the Dash Example Index is to display example apps, each of which are complete minimal examples that can be copied, pasted
and run locally. This app is a multi-page app made with Dash Pages.  It enables each example app to be run as a page of a multi-page app 
while displaying the source code of the complete stand-alone app from the file in the `examples/` folder. 

## Project structure
```
- app.py
- assets
- examples
- lib 
     - make_images
- pages
```

- `app.py` is the main entry point to the app.  After cloning this repo, run `app.py`. It loads the example apps from the `examples` folder, transfers their callbacks
to the main `app` object and creates the dict with the source code. It also has the header footer and callbacks for customizing the 
header and to display example apps in full screen mode.  


-  `assets/` has css that applies to the entire app, plus an image for each app in the `examples` folder.  For consistency,
these images should be created by the utility in the `make_images` folder.  



- `examples/` has the source code for each stand-alone example app.  


- `pages` This is the Dash Pages directory.  The `overview` pages shows the home page with the gallery layout along with the
filters and welcome text box. Each file from the `examples/` folder is registered here and the layout for the "code and show" is defined.  


- `lib/` To make the home page and the "code and show" layouts easier to maintain, they are defined in separate files here. 

- `lib/make_images/` This is the folder for making the app images for each page.

### App Image


Dash Pages  will automatically use the images in the assets folder to create the meta tags.  The images are also used in the 
card grid on the home page.  If no image is provided, then it will default to  `app.png` .

__To generate images:__  

Run  `app_for_image_capture.py`  This creates an app used by a script to update the images.  Each page contains example apps
only with no navigation or headers.
Start this app, then _while it's running,_ run `create_all_images.py` or `create_missing_images.py`

The images will be saved in `make_images/assets/`.  After review, move the image files to the main `assets/` folder.

Until automated testing is set up, recreating all the images is a good way to do manual testing. Review all the images
in `make_images/assets/` after running  `create_all_images.py`.

The `lib/images_not_auto_generated/` is a folder to keep images that don't look great when they are auto generated,
such as the ones with clientside callbacks for smooth animations. 

## Changing the app design

### Home Page
The layout for the current home page is defined in `lib/overview.py`

### Code and Show pages

Each image in the gallery on the home page is a link to the example app's page.  The layout for the page is defined in the `pages/` folder.
For example the "code and show" layout for `examples/colorscales.py` is defined in `pages/colorscales.py`

The "code and show" layouts are functions which you can find in `lib/code_and_show.py`.

Use it to create the layout, for example:

```python
# default side by side layout
layout =  example_app("colorscales.py")

# define a function to display a custom layout 
layout =  example_app("colorscales.py", make_layout=my_custom_layout_function)

# shows the code only
layout = example_app("colorscales.py", run=False)

# shows the app only
layout = example_app("colorscales.py", show_code=False)


```

## Code search

The code search function is defined in `lib/utils.py`

You can make links that will filter the gallery based on search terms.  For example to show only apps that have
a dcc.Slider, the link would look like:
```
https://dash-example-index.herokuapp.com/?code=dcc.Slider
```
