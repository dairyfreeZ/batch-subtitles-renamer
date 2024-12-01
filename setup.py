#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="renamer",
    version="0.1",
    packages=find_packages(exclude=['tests']),
    entry_points={
        "console_scripts": [
            "renamer=src.renamer:main",
        ],
    },
)
