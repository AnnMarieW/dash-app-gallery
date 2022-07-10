import os, sys

sys.path.append(os.path.dirname(sys.path[0]))
import examples
import pytest
import pkgutil
from dash.testing.application_runners import import_app


examples = [
    n for f, n, i in pkgutil.iter_modules(examples.__path__, examples.__name__ + ".")
]


@pytest.mark.parametrize("example", examples)
def test_render_components(dash_duo, example):
    app = import_app(example)
    dash_duo.start_server(app)
