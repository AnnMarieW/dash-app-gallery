"""
Script that saves screenshots of multi-page app pages.
Requires that the app is running on a separate process on localhost:8050

Save images in the update_images/assets directory

"""

import os
from selenium import webdriver
import time

from lib.utils import get_missing_image_names


def snapshot(driver):

    missing_example_apps = get_missing_image_names()
    print(missing_example_apps)

    for page in missing_example_apps:
        path = page.replace("_", "-").lower()
        driver.get(f"http://localhost:8050/{path}")
        time.sleep(5)
        driver.save_screenshot(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)), "assets", f"{page}.png"
            )
        )


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.set_window_size(850, 850)
    try:
        snapshot(driver)
    finally:
        driver.quit()
