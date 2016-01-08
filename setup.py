import os
import sys
from distutils.sysconfig import get_python_lib

from setuptools import find_packages, setup

EXCLUDE_FROM_PACKAGES = []


# Dynamically calculate the version based,
version = __import__('iso3166').get_version()


setup(
    name='iso3166',
    version=version,
    url='https://www.sousouindustries.com/',
    author='Cochise Ruhulessin',
    author_email='cochise.ruhulessin@sousouindustries.com',
    description=("A Python library for ISO 3166 Alpha 2 country code validation."),
    license='Apache Licence 2.0',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    package_data = {'iso3166': ['iso3166.json']},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
