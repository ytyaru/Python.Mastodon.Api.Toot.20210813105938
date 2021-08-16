#!/usr/bin/env python3
# coding: utf8
import requests
import os, sys, argparse, json, urllib.parse, datetime
from string import Template
from abc import ABCMeta, abstractmethod
import mimetypes
# 親ディレクトリをパスに追加する
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from lib import exept_null, Path, FileReader, FileWriter, Authenticator, Api
import media
import unittest
from unittest.mock import MagicMock
import copy
from collections import namedtuple
from string import Template
class TestMediaApp(unittest.TestCase):
    def setUp(self):
        parent = os.path.join(os.path.dirname(__file__), '../src')
        name = 'media.py'
        path = os.path.abspath(os.path.join(parent, name))
        version = '0.0.1'
        Target = namedtuple('Target', 'name path version')
        self.target = Target(name, path, version)
    def test_version(self):
        self.assertEqual(media.App.version(), self.target.version)
    def test_help(self):
        path = os.path.join(os.path.dirname(__file__), '../src/help/media.txt')
        t = Template(FileReader.text(path))
        expected = t.substitute(this=self.target.name, version=self.target.version)
        self.assertEqual(media.App.help(), expected)
    def test_since(self):
        self.assertEqual(media.App.since(), datetime.datetime(2021, 8, 12, 0, 0, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=9))))
    def test_author(self):
        self.assertEqual(media.App.author(), {'name':'ytyaru', 'url':'https://github.com/ytyaru'})
    def test_copyright(self):
        self.assertEqual(media.App.copyright(), '© 2021 ytyaru')
    def test_license(self):
        self.assertEqual(media.App.license(), {'name':'MIT', 'spdx':'MIT', 'url':'https://opensource.org/licenses/MIT'})
    def test_url(self):
        self.assertEqual(media.App.url(), 'https://github.com/ytyaru/Python.Mastodon.Api.Toot.20210812120350')
    def test_license(self):
        self.assertEqual(media.App.license(), {'name':'MIT', 'spdx':'MIT', 'url':'https://opensource.org/licenses/MIT'})
    def test_media(self):
        # https://docs.joinmastodon.org/methods/statuses/media/
        DummyApp = copy.deepcopy(media.App)
        test_data = {"id": "1234", "type":"image", "url":"https://files.test/abc.jpg"}
        DummyApp.media = MagicMock(return_value=test_data) 
        self.assertEqual(media.App.media(), test_data)
        self.assertEqual(media.App.media()['id'], '1234')

if __name__ == "__main__":
    unittest.main()
