# conf.py

import os
import sys

sys.path.insert(0, os.path.abspath('.'))

project = 'ORC'
author = 'James Tasse'
release = '0.8'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = "./_static/images/Satellite-Reentry-Cropped.png"
html_theme_options = {
    'logo_only': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
