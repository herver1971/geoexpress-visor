# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath('..'))


project = 'GeoExpress Visor'
copyright = '2024, Kan Territory & IT'
author = 'Kan Territory & IT'
release = '2.2.0'

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

latex_engine = 'xelatex'
latex_elements = {
    'papersize': 'a4paper',  # Tamaño del papel
    'pointsize': '11pt',  # Tamaño de la fuente
    'passoptionstopackages': r'''
\PassOptionsToPackage{svgnames}{xcolor}
''',
    'fontpkg': r'''
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
''',
    'preamble': r'''
\usepackage[titles]{tocloft}
\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
\setlength{\cftchapnumwidth}{0.75cm}
\setlength{\cftsecindent}{\cftchapnumwidth}
\setlength{\cftsecnumwidth}{1.25cm}
''',
    'sphinxsetup': r'''
TitleColor={[rgb]{0.941, 0.22, 0.38}},  % Aquí se establece el color para los títulos
InnerLinkColor={[rgb]{0.941, 0.22, 0.38}},
OuterLinkColor={[rgb]{0.941, 0.22, 0.38}}
''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
}
latex_show_urls = 'footnote'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'
locale_dirs = ['locale/']   # directorio que contiene los archivos de traducción
gettext_compact = False      # para evitar la compresión de mensajes en un solo archivo

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_static_path = [sphinx_rtd_theme.get_html_theme_path()]
