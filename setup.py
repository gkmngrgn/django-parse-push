#!/usr/bin/env python
# coding=utf-8

import os.path
from distutils.core import setup
import django_parse_push

README = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Web Environment",
    "Framework :: Django",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: System :: Networking",
]

setup(
    name="django-push-notifications",
    version=django_parse_push.get_version(),
    url="https://github.com/jleclanche/django-push-notifications",
    author=u"Gökmen Görgen",
    author_email="gokmen@alageek.com",
    classifiers=CLASSIFIERS,
    description="Parse push support for django",
    download_url="https://github.com/gkmngrgn/django-parse-push/tarball/master",
    packages=[
        "django_parse_push",
    ],
    long_description=README
)
