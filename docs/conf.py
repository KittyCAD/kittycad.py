# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import datetime
import os
import pathlib
import sys
from typing import List

import toml

# The full version, including alpha/beta/rc tags
# Get the version from the pyproject file.

ROOT = pathlib.Path(__file__).parent.parent
PACKAGE_SRC = ROOT / "kittycad"

sys.path.insert(1, os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath("../kittycad"))

# -- Project information -----------------------------------------------------

project = "kittycad"
author = "KittyCAD Team Members"
year = datetime.date.today().year
copyright = str(year) + ", " + author

with open(os.path.abspath("../pyproject.toml"), "r") as f:
    parsed_toml = toml.load(f)
    version = parsed_toml["tool"]["poetry"]["version"]
    version = "v" + version


release = version
language = "en"
default_role = "any"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "autoclasstoc",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.graphviz",
    "sphinx.ext.imgconverter",
    "sphinx.ext.intersphinx",
    "sphinx.ext.linkcode",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "sphinx_rtd_theme",
    "sphinx_copybutton",
    "sphinxext.opengraph",
]

numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path: List[str] = []

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path: List[str] = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "trac"

# pygments_style = "lovelace"
# pygments_dark_style = "one-dark"

# -- autodoc --

autodoc_default_options = {
    "members": True,
    "special-members": True,
    "private-members": True,
    "inherited-members": True,
    "undoc-members": True,
    "exclude-members": "__weakref__",
}

autodoc_inherit_docstrings = True

# -- autosummary --

autosummary_generate = True
autoclass_content = "both"
html_show_sourcelink = False
set_type_checking_flag = True

# -- autosectionlabel --

autosectionlabel_prefix_document = True

# -- intersphinx --

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# This is a function linkcode_resolve(domain, info), which should return the URL
# to source code corresponding to the object in given domain with given information.
# FROM: https://www.sphinx-doc.org/en/master/usage/extensions/linkcode.html
def linkcode_resolve(domain, info):
    if domain != "py":
        return None
    if not info["module"]:
        return None
    filename = info["module"].replace(".", "/")
    return "https://github.com/kittycad/kittycad.py/%s.py" % filename


# Spell checker.
try:
    import enchant  # noqa # pylint: disable=unused-import
except ImportError as ex:
    print(
        "enchant module import failed:\n" "{0}\n" "Spell checking disabled.".format(ex),
        file=sys.stderr,
    )
else:
    extensions.append("sphinxcontrib.spelling")
    spelling_show_suggestions = True
