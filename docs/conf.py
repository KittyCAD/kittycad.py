# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys


sys.path.append(os.path.abspath('../kittycad'))


# -- Project information -----------------------------------------------------

project = 'kittycad'
copyright = '2021, KittyCAD Inc.'
author = 'KittyCAD Inc.'

# The full version, including alpha/beta/rc tags
# Get the version from the poetry file.
import toml

with open(os.path.abspath('../pyproject.toml'), 'r') as f:
    parsed_toml = toml.load(f)
    version = parsed_toml['tool']['poetry']['version']

release = 'v'+ version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',
    'sphinx.ext.intersphinx',
    'sphinx.ext.linkcode'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# Intersphinx configuration.
# FROM: https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#module-sphinx.ext.intersphinx
intersphinx_mapping = {
    'python': ('https://python.readthedocs.io/en/latest/', None),
}

# This is a function linkcode_resolve(domain, info), which should return the URL
# to source code corresponding to the object in given domain with given information.
# FROM: https://www.sphinx-doc.org/en/master/usage/extensions/linkcode.html
def linkcode_resolve(domain, info):
    if domain != 'py':
        return None
    if not info['module']:
        return None
    filename = info['module'].replace('.', '/')
    return "https://github.com/kittycad/kittycad.py/%s.py" % filename


# Spell checker.
try:
    import enchant  # noqa # pylint: disable=unused-import
except ImportError as ex:
    print("enchant module import failed:\n"
          "{0}\n"
          "Spell checking disabled.".format(ex),
          file=sys.stderr)
else:
    extensions.append('sphinxcontrib.spelling')
    spelling_show_suggestions = True
