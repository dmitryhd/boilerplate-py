#!/usr/bin/env python3

# pylint: disable=no-member,no-name-in-module

""" Simple web service boilerplate. """

import flask as fl
import json
import logging
import logging.handlers

settings = {
    'LOGFILE': '/tmp/boilerplate.log'
}


def get_application(settings):
    """
    Configure application from settings.

    :param settings: Settings.
    :return: Flask app
    """
    app = fl.Flask(__name__)
    app.config.update(settings)
    app.debug = True
    def set_routing(app):
        """
        Set url routes to given application.
        """
        app.add_url_rule('/', 'index', index)
        app.add_url_rule('/get-schedule/', 'get_schedule', get_schedule)
        app.add_url_rule('/get_full_graph/', 'get_full_graph', get_full_graph)
        app.add_url_rule('/save_data/', 'save_data', save_data, methods=['POST'])
        # RESTful responses
        # app.add_url_rule('/status/', 'get_status', get_status)

    set_routing(app)

    @app.before_request
    def setup_request():
        pass

    log = logging.getLogger('werkzeug')
    log.setLevel(logging.INFO)
    file_handler = logging.handlers.RotatingFileHandler(
        settings['LOGFILE'], mode='a', maxBytes=10**5, backupCount=1)
    file_handler.setLevel(logging.INFO)
    log.addHandler(file_handler)
    return app


def index():
    """ View """
    return fl.render_template('index.html')


def save_data():
    print(fl.request.values)
    print(fl.request.json)
    return 'ok', 200


def _get_data():
    with open('static/rec_graph.json') as fd:
        gr_json = fd.read()
        return json.loads(gr_json)


def get_full_graph():
    """
    :return:rest query for json
    """
    return fl.jsonify(_get_data())

def get_schedule():
    sched = [
        {'date': '10', 'action': 'start', 'id': 1},
        {'date': '11', 'action': 'start', 'id': 2},
        {'date': '12', 'action': 'end', 'id': 3},
    ]
    return fl.jsonify(schedule=sched)


def run_server():
    app = get_application(settings)
    print('running server')
    app.run()


if __name__ == '__main__':
    run_server()
