# -*- encoding: utf-8 -*-
"""
Python setup file for the companies app.

"""
import os
from setuptools import setup, find_packages
import companies as app


dev_requires = [
    'flake8',
]

install_requires = [
    # User should install requirements
]


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name="valuehorizon-companies",
    version=app.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, app, reusable, companies, valuehorizon',
    author='Quincy Alexander',
    author_email='qalexander@valuehorizon.com',
    url="https://github.com/Valuehorizon/valuehorizon-companies",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'dev': dev_requires,
    },
    test_suite="companies.tests.runtests.runtests"
)
