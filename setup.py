#!/usr/bin/env python3
"""Setup script for potential-winner package."""

from setuptools import setup, find_packages

setup(
    name='potential-winner',
    version='0.1.0',
    description='A Python package',
    author='Charlene',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.7',
    install_requires=[],
)
