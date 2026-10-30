# Build setup aligned with the R2 Tutorials repo (conf.py, requirements.txt, .readthedocs.yaml, _static/js/r2_links.js), 2026-10-25.
# Deliberate differences: project/latex names, release and copyright year, language = 'en' (None gives a warning), fewer comments.
import datetime

extensions = ['myst_parser', 'sphinx_markdown_tables', 'sphinx_design', 'sphinx_copybutton']
myst_enable_extensions = ["linkify", "colon_fence"]
myst_commonmark_only = False
myst_heading_anchors = 3
myst_all_links_external = True
templates_path = ['_templates']

master_doc = 'index'


project = u'R2 training courses'
copyright = u'2026, R2 support team'
author = u'R2 support team'

version = datetime.date.today().strftime('%Y-%m-%d')
release = '2.2.0'
language = 'en'

exclude_patterns = ['_build']
pygments_style = 'sphinx'

import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
def setup(app):
  app.add_css_file("css/r2tutorials.css")
  app.add_js_file("js/r2_links.js")

html_static_path = ['_static']
html_show_sourcelink = True
htmlhelp_basename = 'Testdoc'
html_logo = '_static/images/r2_logo_128.png'
html_favicon = '_static/images/r2favicon.ico'

latex_logo = '_static/images/r2_logo.png'

latex_elements = {
# A4 paper (we are in Europe)
'papersize': 'a4paper',

# Greek letters in the text (alpha, beta): pdflatex does not know them by default (Sphinx 5.3)
'preamble': r'''
\DeclareUnicodeCharacter{03B1}{\ensuremath{\alpha}}
\DeclareUnicodeCharacter{03B2}{\ensuremath{\beta}}
''',

# Put figures exactly where they appear in the text (H) instead of letting them float
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

# The suffix of source filenames.
source_suffix = ['.rst', '.md']
