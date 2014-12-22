#!/usr/bin/env python
# coding=utf-8

import os.path
from distutils.core import setup
import django_parse_push

README = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Environment :: Web Environment",
    "Framework :: Django",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: System :: Networking",
]

setup(
    name="django-parse-push",
    version=django_parse_push.get_version(),
    url="https://github.com/jleclanche/django-push-notifications",
    author=u"Gökmen Görgen",
    author_email="gokmen@alageek.com",
    license="MIT",
    classifiers=CLASSIFIERS,
    description="Parse push support for django",
    download_url="https://github.com/gkmngrgn/django-parse-push/tarball/master",
    packages=[
        "django_parse_push",
    ],
    long_description=README,
    requires=[
        "requests(>=2.5.0)"
    ]
)
