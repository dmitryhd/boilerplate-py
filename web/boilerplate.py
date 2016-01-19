#!/usr/bin/env python3

# pylint: disable=no-member,no-name-in-module

"""
Simple web service boilerplate.
"""

import flask as fl
import argparse

from . log import configure_logger
from . settings import Settings


def get_application(settings):
    """
    Configure application from settings.

    :param settings: Settings.
    :return: Flask app
    """
    app = fl.Flask(__name__)
    app.debug = True
    def set_routing(app):
        """
        Set url routes to given application.
        """
        # Views
        app.add_url_rule('/', 'index', index)
        # REST api
        app.add_url_rule('/get-recommendations/<int:user_id>',
                         'get_recommendations', get_recommendations)

    set_routing(app)
    configure_logger('werkzeug', settings.logfile_location)
    return app


def index():
    """ View """
    return fl.render_template('index.html')


def get_recommendations(user_id):
    recoms = [
        {'item_id': '10'},
        {'item_id': '10'},
        {'item_id': '10'},
        {'item_id': '10'},
    ]
    history = [
        {'item_id': 12},
        {'item_id': 13},
    ]
    return fl.jsonify(recoms=recoms, history=history)


def run_server(port=9000):
    settings = Settings()
    app = get_application(settings)
    app.run(port=port)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=9000)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    run_server(args.port)
