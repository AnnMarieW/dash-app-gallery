import dash
from dash import html

from lib.code_and_show import error_example


dash.register_page(
    __name__,

)

# error file and image
filename = __name__.split("pages.")[1]
image = f"{filename}.png"

# corrected code file
no_error_filename = filename.split("-")[1:]
no_error_filename = "-".join(no_error_filename)


layout = error_example(filename, image, no_error_filename)
