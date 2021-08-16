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
import media
import unittest
from unittest.mock import MagicMock, patch, mock_open
import copy
class TestTootApp(unittest.TestCase):
    def test_version(self):
        self.assertEqual(media.App.version(), '0.0.1')
    def test_help(self):
        self.assertEqual(media.App.help().splitlines()[0], 'Mastodon APIで画像・音声・動画をアップロードする。	0.0.1')
    def test_media(self):
        # https://docs.joinmastodon.org/methods/statuses/
        test_data = {"id": "1234", "type":"image", "url":"https://files.test/abc.jpg"}
        DummyApp = copy.deepcopy(media.App)
        DummyApp.toot = MagicMock(return_value=test_data) 
        self.assertEqual(DummyApp.toot(''), test_data)
        self.assertEqual(DummyApp.toot('')['id'], '1234')

if __name__ == "__main__":
    unittest.main()
