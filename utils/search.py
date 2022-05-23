import os
from pathlib import Path
from utils.init_app import example_source_codes

ROOT_DIR = Path(__file__).parent.parent
EXAMPLE_APPS_DIR = os.path.join(ROOT_DIR, "examples")

"""
Note:  The file names of the example apps must be unique, even if they are in subdirectories.  This will make it 
       possible to match the example app file name with the correct page in the dash.page_registry, even if the 
       file structure for two are different.
"""


def search_code_files(searchterms, case_sensitive):
    """
    returns a list of filenames of the example apps that contain the search terms
    todo: search for exact string, and/or
    """
    filtered = []
    for filename, code in example_source_codes.items():
        if not case_sensitive:
            code = code.lower()
            searchterms = searchterms.lower()

        if searchterms in code:
            filtered.append(filename)
    return filtered
