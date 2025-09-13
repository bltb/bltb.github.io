import os
import sys

sys.path.insert(0, os.path.abspath("."))

project = "bacon lettuce tomato leche"
copyright = "2025, Benjamin Lee"
author = "Benjamin Lee"
release = "0.1"

extensions = [
    "canonical_sphinx",
    "sphinx_last_updated_by_git",
    "sphinx.ext.intersphinx",
    "sphinx_sitemap",
    "sphinxcontrib.mermaid",
]

github_username = "bltb"
github_repository = "bltb.github.io"
github_url = f"https://github.com/{github_username}{github_repository}"

html_context = {
    "github_url": github_url,
    "github_version": "master",
    "github_folder": "/docs/",
}

html_theme_options = {
    "source_edit_link": github_url,
}

disable_feedback_button = True
