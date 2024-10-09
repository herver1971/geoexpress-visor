# docs/latex_template.py

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
\usepackage{eso-pic}  % Paquete para agregar imágenes en el fondo
        \usepackage{graphicx}  % Paquete para manejar gráficos (imágenes)
        \AddToShipoutPictureBG*{%
            \AtPageLowerLeft{%
                \ifnum\value{page}=1  % Solo en la primera página
                    \includegraphics[width=\paperwidth,height=\paperheight]{images/cabeceraKAN.png}
                \fi
            }
        }
''',
    'sphinxsetup': ''' 
        TitleColor={RGB}{240,56,97},
        InnerLinkColor={RGB}{240,56,97},
    ''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
}
