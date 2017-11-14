#!/usr/bin/env python
try:
    from setuptools import setup
    args = {}
except ImportError:
    from distutils.core import setup
    print("""\
*** WARNING: setuptools is not found.  Using distutils...
""")

from setuptools import setup
try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

from os import path
setup(name='Rocket-Launch-Simulator',
      version='0.0.2',
      description='A simple simulator used to predict altitude of a sounding rocket launch',
      long_description= "" if not path.isfile("README.md") else read_md('README.md'),
      author='Hayden Oliver',
      author_email='haydenoliver@gmail.com',
      url='https://github.com/hallover/Rocket-Launch-Simulator',
      license='MIT',
      setup_requires=['pytest-runner',],
      tests_require=['pytest', 'python-coveralls'],
      install_requires=[
          "numpy","matplotlib",
      ],
      packages=['package'],
      # scripts=[''],
      include_package_data=True,
      classifiers=[
          'Development Status :: 1 - planning',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Operating System :: Ubuntu 16.04',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
      ],
)
