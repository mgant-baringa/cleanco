#!/usr/bin/env python

import setuptools

from setuptools import setup

setup(name='cleanco',
      description='Python library to process company names',
      version='1.362',
      license="MIT",
      classifiers = [
         "Topic :: Office/Business",
         "Development Status :: 4 - Beta",
         "Intended Audience :: Developers",
         "License :: OSI Approved :: MIT License",
         "Programming Language :: Python :: 2.7",
         "Programming Language :: Python :: 3.5"
      ],
      url='https://github.com/mgant-baringa/cleanco',
      author='Michael Gant',
      author_email='michael.gant@baringa.com',
      py_modules=['cleanco', 'termdata'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest', 'tox'],
      )
