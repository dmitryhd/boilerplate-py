#!/usr/bin/env python3

# pylint: disable=no-member,no-name-in-module

""" Web interface for lead generator. """

import flask as fl
import json
import logging
import logging.handlers

web_log = logging.getLogger('werkzeug')


def get_application(settings):
    """
    Configure application from settings.

    :param settings: Settings.
    :return: Flask app
    """
    app = fl.Flask(__name__)
    app.settings = settings
    app.config.update(settings)
    app.debug = True

    set_routing(app)

    @app.before_request
    def setup_request():
        pass

    file_handler = logging.handlers.RotatingFileHandler(
        '/tmp/graph.edit.log', mode='a', maxBytes=10**5, backupCount=1)
    file_handler.setLevel(logging.INFO)
    # app.logger.handlers = []
    log = logging.getLogger('werkzeug')
    log.handlers = []
    log.setLevel(logging.INFO)
    log.addHandler(file_handler)
    return app


def set_routing(app):
    """
    Set url routes to given application.
    """
    app.add_url_rule('/', 'graph_edit', graph_edit)
    app.add_url_rule('/get_full_graph/', 'get_full_graph', get_full_graph)
    app.add_url_rule('/save_data/', 'save_data', save_data, methods=['POST'])
    # RESTful responses
    # app.add_url_rule('/status/', 'get_status', get_status)


def save_data():
    print(fl.request.values)
    print(fl.request.json)
    return 'ok', 200


def graph_edit():
    """ View """
    return fl.render_template('graph.html')


def _get_graph():
    with open('static/rec_graph.json') as fd:
        gr_json = fd.read()
        return json.loads(gr_json)


def get_full_graph():
    """
    :return:rest query for json
    """
    return fl.jsonify(_get_graph())


settings = {}


def run_server():
    app = get_application(settings)
    print('running server')
    app.run()


if __name__ == '__main__':
    run_server()
