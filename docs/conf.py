import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'bacon lettuce tomato leche'
copyright = '2025, Benjamin Lee'
author = 'Benjamin Lee'
release = '0.1'

extensions = [
    "canonical_sphinx",
    "sphinx_last_updated_by_git",
    "sphinx.ext.intersphinx",
    "sphinx_sitemap",
    'sphinxcontrib.mermaid',
]

disable_feedback_button = True
