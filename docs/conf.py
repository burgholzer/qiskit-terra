# This code is part of Qiskit.
#
# (C) Copyright IBM 2018.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# pylint: disable=invalid-name

"""Sphinx documentation builder."""

# -- General configuration ---------------------------------------------------

project = "Qiskit"
copyright = "2019, Qiskit Development Team"  # pylint: disable=redefined-builtin
author = "Qiskit Development Team"

# The short X.Y version
version = ""
# The full version, including alpha/beta/rc tags
release = "0.19.2"

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.extlinks",
    "jupyter_sphinx",
    "sphinx_autodoc_typehints",
    "reno.sphinxext",
    "sphinx_panels",
]
templates_path = ["_templates"]

# Number figures, tables and code-blocks if they have a caption.
numfig = True
# Available keys are 'figure', 'table', 'code-block' and 'section'.  '%s' is the number.
numfig_format = {"table": "Table %s"}

# The language for content autogenerated by Sphinx or the default for gettext content translation.
language = None

# Relative to source directory, affects general discovery, and html_static_path and html_extra_path.
exclude_patterns = ["_build", "**.ipynb_checkpoints"]

pygments_style = "colorful"

# Whether module names are included in crossrefs of functions, classes, etc.
add_module_names = False

# A list of prefixes that are ignored for sorting the Python module index
# (e.g., if this is set to ['foo.'], then foo.bar is shown under B, not F).
modindex_common_prefix = ["qiskit."]


# -- Options for HTML output -------------------------------------------------

html_theme = "qiskit_sphinx_theme"  # use the theme in subdir 'theme'
html_last_updated_fmt = "%Y/%m/%d"
html_theme_options = {
    "logo_only": True,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": True,
}
html_static_path = ["_static"]
html_css_files = []


# -- Options for Autosummary and Autodoc -------------------------------------

# Note that setting autodoc defaults here may not have as much of an effect as you may expect; any
# documentation created by autosummary uses a template file (in autosummary in the templates path),
# which likely overrides the autodoc defaults.

autosummary_generate = True
autosummary_generate_overwrite = False
autoclass_content = "both"
