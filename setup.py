#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
# original author: adefossez
# Inspired from https://github.com/kennethreitz/setup.py

from pathlib import Path

from setuptools import setup, find_packages

NAME = 'brainmagick'
DESCRIPTION = (
    'Framework for training deep neural network on MEG and EEG data.')

URL = 'https://github.com/TylerCollison/brainmagick'
EMAIL = 'tylerc2089@hotmail.com'
AUTHOR = 'Tyler Collison'
REQUIRES_PYTHON = '>=3.7.0'
VERSION = '<VERSION>'

HERE = Path(__file__).parent

# http does not work with setup.py
REQUIRED = [i.strip() for i in open("requirements.txt") if "://" not in i]

try:
    with open(HERE / "README.md", encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(),
    install_requires=REQUIRED,
    include_package_data=True,
    license='Creative Commons Attribution-NonCommercial 4.0 International',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)
