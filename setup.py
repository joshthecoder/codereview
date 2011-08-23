#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages

setup(name="github_codereview",
      version="1.0.0",
      description="",
      license="MIT",
      author="Appcelerator, Inc.",
      author_email="jroesslein@appcelerator.com",
      url="http://github.com/appcelerator/codereview",
      packages=['codereview'],
      scripts=['bin/codereview'],
      keywords= "code review github pull requests",
      install_requires=['requests', 'prettytable'],
      zip_safe = True)
