# -*- coding: utf-8 -*-
"""Installer for the paragon.site package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = \
    read('README.rst')

setup(
    name='paragon.site',
    version='0.1',
    description="ct and config for paragon.plone.org",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='Plone',
    author='Philip Bauer',
    author_email='bauer@starzel.de',
    url='http://pypi.python.org/pypi/paragon.site',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['paragon'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'five.pt',
        'Pillow',
        'Plone',
        'plone.api',
        'setuptools',
        'z3c.jbot',
        'plone.app.dexterity [relations]',
        'plone.app.contenttypes',
        'plone.formwidget.multifile',
        'plone.app.referenceablebehavior',
        'plone.formwidget.recaptcha',
        'collective.js.datatables',
        'collective.autopermission',
        'paragon.theme',
        'cioppino.twothumbs',
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
