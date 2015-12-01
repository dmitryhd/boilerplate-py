#!/usr/bin/env python3

# pylint: disable=no-member,no-name-in-module

""" Simple web service boilerplate. """

import flask as fl
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
        app.add_url_rule('/get-schedule/', 'get_schedule', get_schedule)
        app.add_url_rule('/save_data/', 'save_data', save_data, methods=['POST'])
        # app.add_url_rule('/status/', 'get_status', get_status)

    set_routing(app)

    configure_logger('werkzeug', settings.logfile_location)
    return app


def index():
    """ View """
    return fl.render_template('index.html')


def save_data():
    print(fl.request.values)
    print(fl.request.json)
    return 'ok', 200


def get_schedule():
    sched = [
        {'date': '10', 'action': 'start', 'id': 1},
        {'date': '11', 'action': 'start', 'id': 2},
        {'date': '12', 'action': 'end', 'id': 3},
    ]
    return fl.jsonify(schedule=sched)


def run_server(port=9000):
    settings = Settings()
    app = get_application(settings)
    app.run(port=port)


if __name__ == '__main__':
    run_server()
