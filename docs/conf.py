import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'bacon lettuce tomato leche'
copyright = '2025, Benjamin Lee'
author = 'Benjamin Lee'
release = '0.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx_git',
    'sphinx_rtd_theme',
    'sphinxemoji.sphinxemoji',
]

html_theme = 'sphinx_rtd_theme'

todo_include_todos = True
