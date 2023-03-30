import os, sys

sys.path.append(os.path.dirname(sys.path[0]))

# import pytest

from app import app


def test_main_app(dash_duo):
    dash_duo.start_server(app)
