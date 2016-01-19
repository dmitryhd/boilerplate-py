#!/usr/bin/env python3

# pylint: disable=no-member,no-name-in-module

"""
Simple web service boilerplate.
"""

import flask as fl
import argparse
import pandas as pd
import logging
from datetime import datetime

from . log import configure_logger
from . settings import Settings


log = logging.getLogger('werkzeug')
recom = pd.DataFrame()
hist = pd.DataFrame()
user_ids = []


def load_data():
    # mock
    global recom
    global hist
    global user_ids
    log.info('loading data')
    recom = pd.DataFrame({
        'item_id': [1, 2, 3, 4],
        'user_id': [1, 1, 2, 2],
        'img_url': [
            'https://55.img.avito.st/640x480/1299509755.jpg',
            'https://55.img.avito.st/640x480/1299509755.jpg',
            'https://55.img.avito.st/640x480/1299509755.jpg',
            'https://55.img.avito.st/640x480/1299509755.jpg',
        ],
        'url': [
            'https://www.avito.ru/moskva/gruzoviki_i_spetstehnika/gusenichnyy_ekskavator_doosan_dx300lca_yu._koreya_482375232',
            'https://www.avito.ru/moskva/gruzoviki_i_spetstehnika/gusenichnyy_ekskavator_doosan_dx300lca_yu._koreya_482375232',
            'https://www.avito.ru/moskva/gruzoviki_i_spetstehnika/gusenichnyy_ekskavator_doosan_dx300lca_yu._koreya_482375232',
            'https://www.avito.ru/moskva/gruzoviki_i_spetstehnika/gusenichnyy_ekskavator_doosan_dx300lca_yu._koreya_482375232',
        ]
    })
    date = datetime.now()
    hist = pd.DataFrame({
        'item_id': [10, 20, 30, 40],
        'user_id': [1, 1, 2, 2],
        'date': [date] * 4,
        'img_url': [
            'https://55.img.avito.st/640x480/1299509755.jpg',
            'https://55.img.avito.st/640x480/1299509755.jpg',
            'https://55.img.avito.st/640x480/1299509755.jpg',
            'https://55.img.avito.st/640x480/1299509755.jpg',
        ],
        'url': [
            'https://www.avito.ru/moskva/gruzoviki_i_spetstehnika/gusenichnyy_ekskavator_doosan_dx300lca_yu._koreya_482375232',
            'https://www.avito.ru/moskva/gruzoviki_i_spetstehnika/gusenichnyy_ekskavator_doosan_dx300lca_yu._koreya_482375232',
            'https://www.avito.ru/moskva/gruzoviki_i_spetstehnika/gusenichnyy_ekskavator_doosan_dx300lca_yu._koreya_482375232',
            'https://www.avito.ru/moskva/gruzoviki_i_spetstehnika/gusenichnyy_ekskavator_doosan_dx300lca_yu._koreya_482375232',
        ]
    })
    user_ids = [1, 2, 10, 20]
    log.info('loading data: done!')


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
    rec = recom[recom.user_id == user_id].to_dict('records')
    for item in rec:
        for key in item:
            try:
                item[key] = int(item[key])
            except:
                pass
    history = hist[hist.user_id == user_id].to_dict('records')
    for item in history:
        for key in item:
            try:
                item[key] = int(item[key])
            except:
                pass
    return fl.jsonify(recoms=rec,
                      history=history,
                      user_ids=user_ids)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=9000)
    return parser.parse_args()


def run_server(port=9000):
    settings = Settings()
    app = get_application(settings)
    load_data()
    app.run(port=port)


if __name__ == '__main__':
    args = parse_args()
    run_server(args.port)
