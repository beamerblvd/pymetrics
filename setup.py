#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    unicode_literals,
)

import codecs
from setuptools import (
    find_packages,
    setup,
)

from pymetrics import __version__


def readme():
    with codecs.open('README.rst', 'rb', encoding='utf8') as f:
        return f.read()


tests_require = [
    'freezegun',
    'pytest',
    'pytest-cov',
    'pytest-runner',
    'mock',
    'more-itertools~=5.0',  # We must pin this, because 6.0 requires Python 3.
    'mypy;python_version>"3.4"',
]

setup(
    name='pymetrics',
    version=__version__,
    author='Eventbrite, Inc.',
    author_email='opensource@eventbrite.com',
    description='Versatile metrics collection for Python',
    long_description=readme(),
    url='https://github.com/eventbrite/pymetrics',
    packages=list(map(str, find_packages(include=['pymetrics', 'pymetrics.*']))),
    package_data={str('pymetrics'): [str('py.typed')]},  # PEP 561
    zip_safe=False,  # PEP 561
    include_package_data=True,
    install_requires=[
        'attrs>=17.4,<20',
        'conformity~=1.26,>=1.26.1',
        'enum34;python_version<"3.4"',
        'six',
        'typing;python_version<"3.5"',
    ],
    tests_require=tests_require,
    test_suite='tests',
    extras_require={
        'testing': tests_require,
        'docs': ['sphinx~=2.2;python_version>="3.6"'],
    },
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
    ],
    project_urls={
        'Documentation': 'https://pymetrics.readthedocs.io',
        'Issues': 'https://github.com/eventbrite/pymetrics/issues',
        'CI': 'https://travis-ci.org/eventbrite/pymetrics/',
    },
)
