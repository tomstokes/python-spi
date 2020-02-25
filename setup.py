#!/usr/bin/env python

import setuptools
from distutils.core import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(name="python3-spi",
      version="0.3.0",
      description="Python interface for SPI communications",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="Tom Stokes, Tom Egan",
      author_email="tom@tomegan.tech",
      url="https://github.com/tkegan/python-spi",
      license="MIT",
      py_modules=['spi'])
