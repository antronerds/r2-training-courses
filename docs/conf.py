import datetime

extensions = []
templates_path = ['_templates']

master_doc = 'index'

project = u'R2 training courses'
copyright = u'2018, R2 support team'
author = u'R2 support team'

version = datetime.date.today().strftime('%Y-%m-%d')
release = '2.0.2'
language = None

exclude_patterns = ['_build']
pygments_style = 'sphinx'

import sphinx_rtd_theme
html_theme = "default"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
def setup(app):
 app.add_stylesheet( "css/r2tutorials.css" )
# from http://stackoverflow.com/questions/32079200/how-do-i-set-up-custom-styles-for-restructuredtext-sphinx-readthedocs-etc/32079202#32079202

html_static_path = ['_static']
html_show_sourcelink = True
htmlhelp_basename = 'Testdoc'
html_logo = '_static/images/r2_logo_128.png'
html_favicon = '_static/images/r2favicon.ico'

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
# Changed this to a4; we're in Europe ;-)
'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
# default below is float; we want position as is: H
#'figure_align': 'htbp', 
'figure_align': 'H', 
}

latex_documents = [
  (master_doc, 'Test.tex', u'R2 Training Courses',
   u'The R2 support team', 'manual'),
]

man_pages = [
    (master_doc, 'test', u'R2 Training Courses',
     [author], 1)
]

texinfo_documents = [
  (master_doc, 'Test', u'R2 Training Courses',
   author, 'Test', 'R2 Training Courses',
   'Miscellaneous'),
]

from recommonmark.parser import CommonMarkParser

# The suffix of source filenames.
source_suffix = ['.rst', '.md']

source_parsers = {
	'.md': CommonMarkParser,
}
