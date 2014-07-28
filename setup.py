#!/usr/bin/env python
# -*- coding: utf-8 -*-
# $Id$

from setuptools import setup

setup(
    name='django-i18n-install',
    version='0.1',
    description=''
    'A helper to run django compilemessages command before install',
    author='Dmitri Bogomolov',
    author_email='4glitch@gmail.com',
    url='https://github.com/g1itch/django-i18n-install',

    packages=['django_i18n_install'],
    package_dir={'django_i18n_install': 'src'},

    install_requires=['setuptools>=0.7', 'Django'],

    entry_points={
        'distutils.commands': [
            'django_compilemessages = '
            'django_i18n_install.commands:django_compilemessages'
        ]},

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Framework :: Setuptools Plugin',
        'Topic :: Software Development :: Internationalization'
    ]
)
