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
from unittest.mock import MagicMock, patch, mock_open
import copy
from collections import namedtuple
from string import Template
class TestMedia(unittest.TestCase):
    def test_api_url(self):
        test_data = 'test.host.com'
        mock_io = mock_open(read_data=test_data)
        with patch('builtins.open', mock_io):
            actual = Api().BaseUrl
            parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            parent = os.path.join(parent, 'src')
            path = os.path.join(parent, 'host.txt')
            path = os.path.expandvars(os.path.expanduser(path))
            mock_io.assert_called_once_with(path, mode='r', encoding='utf-8')
            self.assertEqual(actual, f'https://{test_data}/')
            self.assertEqual(media.Media().ApiUrl, f'https://{test_data}/api/v1/media')
    def test_media(self):
        # https://docs.joinmastodon.org/methods/statuses/media/
        app = media.Media()
        test_data = {"id": "1234", "type":"image", "url":"https://files.test/abc.jpg"}
        app.media = MagicMock(return_value=test_data)
        res = app.media('')
        self.assertEqual(res, test_data)
        self.assertEqual(res['id'], '1234')

if __name__ == "__main__":
    unittest.main()
