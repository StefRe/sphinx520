import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import SampleModule

# -- Project information -----------------------------------------------------

project = 'sample-project'
copyright = '2020, <Author>'
author = '<Author>'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    ]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'

html_static_path = []


