# ============================================================
# VIRTUAL ENVIRONMENTS
# ============================================================


# 1. What is a Virtual Environment?
#
# A virtual environment is an isolated Python environment
# created for a specific project.
#
# It allows each project to have its own Python packages
# and dependencies without affecting other projects.


# ============================================================
# 2. Why Do We Need a Virtual Environment?
# ============================================================

# Different projects may require different versions
# of the same package.
#
# Example:
#
# Project A -> pandas 2.x
# Project B -> pandas 3.x
#
# Installing everything globally can cause dependency
# conflicts.
#
# A virtual environment keeps each project's dependencies
# isolated.


# ============================================================
# 3. Create a Virtual Environment
# ============================================================

# Create a virtual environment named .venv:
#
# python -m venv .venv


# ============================================================
# 4. Activate the Virtual Environment
# ============================================================

# Windows:
#
# .venv\Scripts\activate
#
# After activation, the terminal usually shows:
#
# (.venv)
#
# This means the virtual environment is active.


# ============================================================
# 5. pip
# ============================================================

# pip is Python's package manager.
#
# It is used to install, update, uninstall and manage
# Python packages.


# Install a package:
#
# pip install pandas


# ============================================================
# 6. pip list
# ============================================================

# Shows the packages installed in the currently active
# Python environment.
#
# Command:
#
# pip list


# ============================================================
# 7. requirements.txt
# ============================================================

# requirements.txt contains the packages/dependencies
# required by a project.
#
# Create it from the current environment:
#
# pip freeze > requirements.txt
#
# Install all dependencies from the file:
#
# pip install -r requirements.txt


# ============================================================
# 8. Uninstall a Package
# ============================================================

# pip uninstall <package_name>
#
# Example:
#
# pip uninstall pandas


# ============================================================
# 9. Deactivate
# ============================================================

# Leave the virtual environment:
#
# deactivate


# ============================================================
# QUICK FLOW
# ============================================================

# Create:
# python -m venv .venv
#
# Activate:
# .venv\Scripts\activate
#
# Install packages:
# pip install pandas
#
# See installed packages:
# pip list
#
# Save dependencies:
# pip freeze > requirements.txt
#
# Install dependencies:
# pip install -r requirements.txt
#
# Deactivate:
# deactivate