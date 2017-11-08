#!/usr/bin/env python3

import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


requires=[
    'pyaml',
]

setup(
    name='django-project-generator',
    version='0.1',
    author='Georgy Bazhukov',
    author_email='georgy.bazhukov@gmail.com',
    description='Library provides pixelation for images',
    long_description="""
# Django Project Generator
""",
    url='https://github.com/bugov/django-project-generator',
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite="tests",
    requires=requires,
    tests_require=requires + ['pytest'],
    setup_requires=requires + ['pytest-runner'],
    cmdclass = {'test': PyTest},
)
