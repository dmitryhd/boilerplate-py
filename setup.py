#!/usr/bin/env python3

""" Install avitocrm as pypi package. """

from setuptools import setup, find_packages
from os import path
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
cur_dir = path.dirname(path.realpath(__file__))
install_reqs = parse_requirements(
    path.join(cur_dir, "requirements.txt"),
    session=False)

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

from web import __version__

setup(
    name='some pack',
    version=__version__,
    description='Just simple flask application',
    long_description='Just simple flask application',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=reqs,
)