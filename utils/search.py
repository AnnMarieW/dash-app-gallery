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


def search_code_files(searchterms, case_sensitive, search_type="and"):
    """
    returns a list of filenames of the example apps that contain the search terms
    """

    searchterms = searchterms.split()
    if not case_sensitive:
        searchterms = [terms.lower() for terms in searchterms]

    # initialize the index of filenames of code with the search terms
    index = {term: set() for term in searchterms}

    for filename, code in example_source_codes.items():
        if not case_sensitive:
            code = code.lower()

        # build index of filenames of code with the search terms
        for term in searchterms:
            if term in code:
                index[term].add(filename)

    search_results = [index.get(term, set()) for term in searchterms]

    if search_type == "and":
        return set.intersection(*search_results)
    return set.union(*search_results)
