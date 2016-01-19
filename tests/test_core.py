#!/usr/bin/env python3

""" Unittest file for Web server. """

import unittest
import json
import sys
sys.path.append('.')
sys.path.append('..')

import web


class TestWeb(unittest.TestCase):
    """ Basic test of main page view. """
    @classmethod
    def setUpClass(cls):
        """ Init test app """
        settings = web.Settings()
        app = web.get_application(settings)
        cls.app = app.test_client()

    def get(self, url):
        """ :returns: utf8 string, containig html code of url. """
        return self.app.get(url).data.decode('utf8')

    def get_json(self, url):
        """ :returns: dict. """
        data_text = self.get(url)
        return json.loads(data_text)

    def get_and_check(self, url):
        """ :returns: utf8 string and check not 404. """
        html = self.get(url)
        self.assertNotIn('404 Not Found', html)
        return html

    def test_index(self):
        """ Web: get main page. """
        main_page = self.get_and_check('/')
        self.assertIn('Recommended', main_page)
