"""
This is the example  index
"""

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


text = """
# Index

### DataTable
 - [Hiding columns based on screen size](https://community.plotly.com/t/how-to-hide-datatable-columns-based-on-screen-size/60582)
 - [Disply Links in a DataTable](https://gist.github.com/AnnMarieW/6cd86077a0eaf2441057c862e074c074)

### dcc.Markdown
 - [Use dcc.Link in a dcc.Markdown component for high performance links that don't refresh the page ](https://gist.github.com/AnnMarieW/b5269c177cc3dfed06766aded802f664)
 
 
### Images
 - [How to display images in a Dash app](https://community.plotly.com/t/how-to-embed-images-into-a-dash-app/61839)
 - [Convert HTML to an image and download](https://community.plotly.com/t/download-component-as-image-using-clientside-callback/59503/4)


### Common Error Messages
-  [Invalid argument `figure` passed into Graph with ID...'](/error-getting-started)
-  [Callback error updating...](/error2-getting-started)
-  [The children property of a component is a list of lists, instead of just a list....](/error-figures-with-ctx)


### Interactive Tutorials
- [Legend and annotations positioning in Plotly figures](https://plotly-annotations.herokuapp.com/)
- [How to format numbers in the DataTable](https://formattable.pythonanywhere.com/)
- [Dash Bootstrap Cheatsheet](https://dashcheatsheet.pythonanywhere.com/)


"""


layout = dcc.Markdown(text, className="p-4 mx-2", dangerously_allow_html=True)
