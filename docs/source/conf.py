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

import codecs
import os.path

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

def get_short_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__short_version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

# -- Project information -----------------------------------------------------

project = u'Xena OpenAutomation Python API'
copyright = u'2022, Xena Networks'
author = u'Xena Networks'
title = u'Xena OpenAutomation Python API Documentation'

# The full version, including alpha/beta/rc tags.
release = get_version("../../xoa_driver/__init__.py")

# The short X.Y version.
version = get_short_version("../../xoa_driver/__init__.py")


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
    'sphinx.ext.todo',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.extlinks',
    "sphinx_inline_tabs",
    'sphinx_copybutton',
    "sphinx_remove_toctrees",
]
add_module_names = False
autodoc_default_options = {
    'member-order': 'bysource',
    'private-members': False,
    'undoc-members': False,
    'show-inheritance': True
}
autodoc_typehints = 'signature'
autodoc_typehints_format = 'short'
autodoc_inherit_docstrings = True
todo_include_todos = True
autosectionlabel_prefix_document = True

# The suffix(es) of source filenames.
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# These patterns also affect html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The master toctree document.
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# -- Options for HTML output -----------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = 'sphinx_book_theme'

# Output file base name for HTML help builder.
htmlhelp_basename = 'xoa_driver_doc'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = title

# The path to the HTML logo image in the static path, or URL to the logo, or ''.
html_logo = './_static/xoa_logo.png'

html_favicon = './_static/xoa_favicon_16.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


html_show_copyright = True
html_show_sphinx = False

html_theme_options = {
    "repository_url": "https://github.com/xenanetworks/open-automation-python-api",
    "use_repository_button": True,
    "home_page_in_toc": True,
    "show_toc_level": 2,
    "use_download_button": True,
    "show_navbar_depth": 2,
}

html_split_index = True


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
    (master_doc, 'xoa_driver_doc', title, author, 'xoa_driver_doc', 'Xena OpenAutomation high-level and low-level Python APIs and code examples for Xena TGA testers.', 'Miscellaneous'),
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


# -- Options for LaTeX output -----------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '12pt',

# Additional stuff for the LaTeX preamble.
#'preamble': r'',

# Latex figure (float) alignment
#'figure_align': 'htbp',

#'printindex': r'\def\twocolumn[#1]{#1}\printindex',
'makeindex': r'\usepackage[columns=1]{idxlayout}\makeindex',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(master_doc, 'xoa_driver_doc.tex', title, author, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = './_static/pdf_logo.png'

# -- Options for manual page output -----------------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'xoa_driver_doc', title, [author], 1)
]


# -- Options for EPUB output -----------------------------------------------------
epub_title = title + ' ' + release
epub_author = author
epub_publisher = 'https://xenanetworks.com'
epub_copyright = copyright
epub_show_urls = 'footnote'
epub_basename = 'xoa_driver_doc'

# Remove auto-generated API docs from sidebars. They take too long to build.
remove_from_toctrees = ["api_doc/_autosummary/*"]