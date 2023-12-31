# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Belectric's BESS Boards"
copyright = '2023, Louis Green'
author = 'Louis Green'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
# html_static_path = ['_static']
html_theme_options = {
    "bodyfont": "Century Gothic",
    "headfont": "Century Gothic",
    "textcolor":"black",
    "bgcolor":"#dddddd",
    "sidebarbgcolor":"#f9b9b9",

}
