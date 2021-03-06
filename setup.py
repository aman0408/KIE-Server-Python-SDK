#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "requests"
]

test_requirements = [ ]

setup(
    author="Aman Agrawal",
    author_email='amanagrawal04081999@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='kie_server_py',
    name='kie_server_py',
    packages=find_packages(include=['kie_server_py', 'kie_server_py.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/aman0408/kie_server_py',
    version='0.1.0',
    zip_safe=False,
)
