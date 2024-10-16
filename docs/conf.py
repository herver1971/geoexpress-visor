# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath('.'))


project = 'GeoExpress Visor'
copyright = '2024, Kan Territory & IT'
author = 'Kan Territory & IT'
release = '2.2.0'

# Importar el diccionario latex_template
from latex_template import latex_elements

latex_engine = 'xelatex'
latex_elements = latex_elements

latex_show_urls = 'footnote'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	'sphinx.ext.autodoc',
	'sphinx.ext.todo',
	'sphinx.ext.autosummary',
	'sphinxcontrib.openapi',
	'sphinx.ext.coverage',
	'sphinx.ext.doctest',
	'sphinx.ext.intersphinx',
	'sphinx.ext.viewcode',
	'sphinx.ext.napoleon'
]


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'
locale_dirs = ['locale/']   # directorio que contiene los archivos de traducción
gettext_compact = False      # para evitar la compresión de mensajes en un solo archivo

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_static_path = [sphinx_rtd_theme.get_html_theme_path(), '_static']
