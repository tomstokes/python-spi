#!/usr/bin/env python

import setuptools
from distutils.core import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(name="python3-spi",
    version="0.3.1",
    description="Python interface for SPI communications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tom Stokes, Tom Egan",
    author_email="tom@tomegan.tech",
    url="https://github.com/tkegan/python-spi",
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Embedded Systems',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=2.7, !=3.0.*, <4',
    py_modules=['spi'])
