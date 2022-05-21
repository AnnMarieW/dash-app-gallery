from importlib import import_module
from inspect import getsource
import re
import uuid
import ast


from dash import html, dcc, callback
import dash_bootstrap_components as dbc

from utils.search_code import sourcecode


def example_app(filename, make_layout=None, run=True, show_code=True):
    """
    Creates the "code and show layout for an example dash app.

    - `filename`:
       The path to the file with the sample app code.

    - `make_layout`:
        A function which takes as attributes the code string and the live app and returns a
        layout.  The default layout displays the code side-by-side with the live app on large screens
        or app first followed by the code on smaller screens.

    - `run`:
        bool (default: True) Whether to run the app

    - `show_code`:
        bool (default: True) Whether to show the code

    """

    code = sourcecode[filename]

    run_app = _run_code(code) if run else ""

    # Removes the id prefix
    code = code.replace(filename + "-x-", "")
    code = code if show_code else ""

    if make_layout is not None:
        return make_layout(code, run_app)
    return make_side_by_side(code, run_app)


def make_side_by_side(code, show_app):
    """
    This is the default layout for the "code and show"
    It displays the app and the code side-by-side on large screens, or
    the app first, followed by the code on smaller screens.
    It also has a dcc.Clipboard to copy the code.
    """
    # make a unique id for clipboard
    clipboard_id = str(uuid.uuid4())

    clipboard_style = {
        "right": 0,
        "position": "absolute",
        "top": 0,
        "backgroundColor": "#f6f6f6",
        "color": "#2f3337",
        "padding": 4,
    }
    code_card = html.Div(
        [
            dcc.Markdown(f"```python\n{code}```\n"),
            dcc.Clipboard(
                target_id=f"{clipboard_id}",
                style=clipboard_style,
            ),
        ],
        id=f"{clipboard_id}",
        style={"position": "relative"},
    )

    return dbc.Row(
        [
            dbc.Col(dbc.Card(show_app, style={"padding": "10px"}), width=12, lg=6)
            if show_app
            else None,
            dbc.Col(
                dbc.Card(
                    [code_card], style={"max-height": "800px", "overflow": "auto"}
                ),
                width=12,
                lg=6,
            )
            if code
            else None,
        ]
    )


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
    md_code = dcc.Markdown(f"```python\n{code}```\n")
    return dbc.Row(
        [
            dbc.Col(dbc.Card(show_app, style={"padding": "10px"}), width=12)
            if show_app
            else None,
            dbc.Col(
                dbc.Card([md_code], style={"max-height": "600px", "overflow": "auto"}),
                width=12,
            )
            if code
            else None,
        ]
    )


def _run_code(code):
    scope = {"callback": callback}

    code = code.replace("app.layout", "layout")
    code = code.replace("app.callback", "callback").replace(
        "app.clientside_callback", "clientside_callback"
    )

    # todo use regular expressions to remove the entire line with app.server
    if "app.server" in code:
        code = code.replace("server = app.server", "")

    if "layout" in code:
        # Remove the app instance in the code block otherwise app.callbacks don't work
        tree = ast.parse(code)
        new_tree = RemoveAppAssignment().visit(tree)
        exec(compile(new_tree, filename="<ast>", mode="exec"), scope)
        return html.Div(scope["layout"])


class RemoveAppAssignment(ast.NodeTransformer):
    """
    Remove the app instance from a code block otherwise app.callback` doesn't work. If `app` is defined locally
    within the code block, then it overrides the `app` passed in to the scope.
    """

    def visit_Assign(self, node):
        if hasattr(node, "targets") and "app" in [
            n.id for n in node.targets if hasattr(n, "id")
        ]:
            return None
        return node


def _remove_prefix(page, code):
    """
    Dash requires all ids to be unique, so for multi-page apps it's common to add a prefix to the id.
    The convention for ids in this app is to use the module name followed by "-x-" then the simple id name.
    This function will strip the prefix so that only the simple ID names are displayed.

    For example `id="module_name-x-button"` will display as `id="button"`
    """
    prefix = page.split(".")[-1] + "-x-"
    return code.replace(prefix, "")
