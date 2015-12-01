#!/usr/bin/env python3

""" Car recommendation entry point. """

__author__ = 'dkhodakov'

import argparse

from . import __version__
from . import boilerplate as bp
from . import settings


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=settings.DEFAULT_PORT)
    parser.add_argument('-v', '--version', action='version',
                        version=__version__)
    return parser.parse_args()


def main():
    args = parse_args()
    bp.run_server(args.port)
