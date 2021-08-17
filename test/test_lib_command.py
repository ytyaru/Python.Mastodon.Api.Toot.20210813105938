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
from lib import exept_null, Path, FileReader, FileWriter, Authenticator, Api, Command
#import media
import unittest
from unittest.mock import MagicMock, patch, mock_open
import copy
from collections import namedtuple
from string import Template
import datetime
class TestLibCommand(unittest.TestCase):
    def setUp(self):
        parent = os.path.join(os.path.dirname(__file__), '../src')
        name = 'lib.py'
        path = os.path.abspath(os.path.join(parent, name))
        version = '0.0.1'
        Target = namedtuple('Target', 'name path version')
        self.target = Target(name, path, version)
    def test_version(self):
        self.assertEqual(Command().Version, self.target.version)
    def test_help(self):
        with self.assertRaises(FileNotFoundError):
            Command().Help
#        path = os.path.join(os.path.dirname(__file__), '../src/help/media.txt')
#        t = Template(FileReader.text(path))
#        expected = t.substitute(this=self.target.name, version=self.target.version)
#        self.assertEqual(Command().Help, expected)
    def test_since(self):
        self.assertEqual(Command().Since, datetime.datetime(2021, 8, 12, 0, 0, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=9))))
    def test_author(self):
        self.assertEqual(Command().Author, {'name':'ytyaru', 'url':'https://github.com/ytyaru'})
    def test_copyright(self):
        self.assertEqual(Command().Copyright, '© 2021 ytyaru')
    def test_license(self):
        self.assertEqual(Command().License, {'name':'MIT', 'spdx':'MIT', 'url':'https://opensource.org/licenses/MIT'})
    def test_url(self):
        self.assertEqual(Command().Url, 'https://github.com/ytyaru/Python.Mastodon.Api.Toot.20210812120350')

if __name__ == "__main__":
    unittest.main()
