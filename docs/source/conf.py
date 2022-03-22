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
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../../'))

# import pkg_resources


# -- Project information -----------------------------------------------------

project = u'xoa-driver'
copyright = u'2022, Xena Networks'
author = u'Artem Constantinov, Ron Ding, Leonard Yu'


# The full version, including alpha/beta/rc tags.
release = '1.0'
# The short X.Y version.
version = '1.0b3'


# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
]

# The suffix(es) of source filenames.
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# These patterns also affect html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -----------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = 'sphinx_rtd_theme'

# Output file base name for HTML help builder.
htmlhelp_basename = 'xoadriverdoc'



# -- Options for Texinfo output -----------------------------------------------------

# This config value contains the locations and names of other projects that should be linked to in this documentation.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

intersphinx_disabled_domains = ['std']

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'xoadriverdoc', u'Xena OpenAutomation Python API Documentation', author, 'xoadriverdoc', 'Xena OpenAutomation high-level and low-level Python APIs and code examples for Xena TGA testers.', 'Miscellaneous'),
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


# -- Options for LaTeX output -----------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(master_doc, 'xoadriverdoc.tex', u'Xena OpenAutomation Python API Documentation', u'Artem Constantinov, Ron Ding, Leonard Yu', 'manual'),
]


# -- Options for manual page output -----------------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'xoadriverdoc', u'Xena OpenAutomation Python API Documentation', [author], 1)
]


# -- Options for EPUB output -----------------------------------------------------
epub_show_urls = 'footnote'
epub_basename = 'xoadriverdoc'