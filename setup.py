# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ytbingo',
    version='0.0.1',
    description='Generate bingo boards from previous transcripts.',
    long_description=readme,
    author='George Campbell',
    author_email='abersnaze@gmail.com',
    url='https://github.com/abersnaze/youtube-bingo',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
