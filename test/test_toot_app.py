#!/usr/bin/env python3
# coding: utf8
#import requests
#import os, sys, argparse, json, urllib.parse, datetime
#from string import Template
#from abc import ABCMeta, abstractmethod
#import mimetypes
import os, sys
# 親ディレクトリをパスに追加する
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from lib import exept_null, Path, FileReader, FileWriter, Authenticator, Api
import toot
import unittest
from unittest.mock import MagicMock, patch, mock_open
import copy
from collections import namedtuple
from string import Template
class TestTootApp(unittest.TestCase):
    def setUp(self):
        parent = os.path.join(os.path.dirname(__file__), '../src')
        name = 'toot.py'
        path = os.path.abspath(os.path.join(parent, name))
        version = '0.0.1'
        Target = namedtuple('Target', 'name path version')
        self.target = Target(name, path, version)
    def test_version(self):
        self.assertEqual(toot.App().Version, self.target.version)
    def test_help(self):
        path = os.path.join(os.path.dirname(__file__), '../src/help/toot.txt')
        t = Template(FileReader.text(path))
        expected = t.substitute(this=self.target.name, version=self.target.version)
        self.assertEqual(toot.App().Help, expected)
    def test_toot(self):
        # https://docs.joinmastodon.org/methods/statuses/
        test_data = {"id": "1234", "created_at":"2020-01-01T00:00:00+0900", "content":"<p>テスト内容。</p>"}
        app = toot.App()
        app.toot = MagicMock(return_value=test_data) 
        self.assertEqual(app.toot(''), test_data)
        self.assertEqual(app.toot('')['id'], '1234')

if __name__ == "__main__":
    unittest.main()
