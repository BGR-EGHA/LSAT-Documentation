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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'LSAT PM'
copyright = '2022, Federal Institute for Geosciences and Natural Resources'
author = 'Federal Institute for Geosciences and Natural Resources'

# The full version, including alpha/beta/rc tags
release = '1.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'nature'

# If given, this must be the name of an image file (path relative to the 
# configuration directory) that is the logo of the docs, or URL that points an
# image file for the logo. It is placed at the top of the sidebar; its width
# should therefore not exceed 200 pixels. Default: None.
html_logo = 'LSAT_logo.png'

# Suffix for section numbers. Default: ". ". Set to " " to suppress the final
# dot on section numbers.
html_secnumber_suffix = " "

# If numfig = True, figures, tables and code-blocks are automatically numbered
# if they have a caption. The numref role is enabled. Obeyed so far only by
# HTML and LaTeX builders. Default is False.
numfig = True