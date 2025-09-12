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

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

todo_include_todos = True

html_context = {
    "display_github": True,
    "github_user": "bltb",
    "github_repo": "bltb.github.io",
    "github_version": "master",
    "conf_py_path": "/docs/",
}
