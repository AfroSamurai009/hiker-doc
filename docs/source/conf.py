# Configuration file for the Sphinx documentation builder.

# -- Project information
import os
import sys

# Add the docs directory to the path
sys.path.insert(0, os.path.abspath(".."))
# Add the hikerapi package directory to the path
sys.path.insert(0, os.path.abspath("../hikerapi"))

from __version__ import __version__

project = "HikerAPI"
copyright = "2021, HikerAPI"
author = "HikerAPI"

release = __version__
version = __version__

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.viewcode",  # Add viewcode extension
]

# Add autodoc settings
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"

# -- Options for EPUB output

epub_show_urls = "footnote"

pygments_style = "sphinx"
