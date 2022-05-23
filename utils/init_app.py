import os
from pathlib import Path
from importlib import import_module
from inspect import getsource


EXAMPLE_APPS_DIR_NAME = "examples"
ROOT_DIR = Path(__file__).parent.parent
EXAMPLE_APPS_DIR = os.path.join(ROOT_DIR, EXAMPLE_APPS_DIR_NAME)
APP_ASSETS_DIR = os.path.join(ROOT_DIR, "assets")


def file_names():
    names = []
    for filename in os.listdir(EXAMPLE_APPS_DIR):
        if not filename.startswith("_") and filename.endswith(".py"):
            filename = filename.replace(".py", "")
            if filename in names:
                raise Exception(
                    f"filenames must be unique.  `{filename}.py` already exists"
                )
            names.append(filename)
    return names


file_names = file_names()

example_modules = {p: import_module(f"{EXAMPLE_APPS_DIR_NAME}.{p}") for p in file_names}
example_apps = {p: m.app for p, m in example_modules.items()}
example_source_codes = {p: getsource(m) for p, m in example_modules.items()}


def get_app_image_names():
    app_images = [
        filename.replace(".png", "")
        for filename in os.listdir(APP_ASSETS_DIR)
        if not filename == "app" and filename.endswith(".png")
    ]
    app_images.sort()
    return app_images


def get_missing_image_names():
    images = get_app_image_names()
    missing = [app for app in file_names if app not in images]
    return missing
