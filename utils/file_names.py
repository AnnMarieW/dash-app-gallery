import os
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
EXAMPLE_APPS_DIR = os.path.join(ROOT_DIR, "pages", "examples")
APP_ASSETS_DIR = os.path.join(ROOT_DIR, "assets")


def get_example_app_names():
    example_apps = [
        filename.replace(".py", "")
        for filename in os.listdir(EXAMPLE_APPS_DIR)
        if not filename.startswith("_") and filename.endswith(".py")
    ]
    example_apps.sort()
    return example_apps


def get_app_image_names():
    app_images = [
        filename.replace(".png", "")
        for filename in os.listdir(APP_ASSETS_DIR)
        if not filename == "app" and filename.endswith(".png")
    ]
    app_images.sort()
    return app_images


def get_missing_image_names():
    apps = get_example_app_names()
    images = get_app_image_names()
    missing = [app for app in apps if app not in images]
    return missing
