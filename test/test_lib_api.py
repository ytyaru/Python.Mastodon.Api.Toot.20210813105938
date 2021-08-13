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
import unittest
from unittest.mock import MagicMock, patch, mock_open
import copy
class TestApi(unittest.TestCase):
    def test_auth(self):
        self.assertIsInstance(Api().Auth, Authenticator)
    def test_base_url_file(self):
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
    @patch("builtins.open", MagicMock(side_effect=Exception()))
    def test_base_url_default(self):
        self.assertEqual(Api().BaseUrl, 'https://mstdn.jp/')
    """
    def test_header(self):
        parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        parent = os.path.join(parent, 'src')
        path_ua = os.path.join(parent, 'user-agent.txt')
        path_ua = os.path.expandvars(os.path.expanduser(path_ua))
        user_agent = FileReader.text(path_ua)

        test_data = 'xxxxxxxxxxxxxxxxxx'
        mock_io = mock_open(read_data=test_data)
        with patch('builtins.open', mock_io):
            path_token = os.path.join(parent, 'token.txt')
            actual = FileReader.text(path_token)
            expected = {
                'User-Agent': user_agent ,
                'Authorization': f'Bearer {Api().Auth.Token}'
            }
            self.assertEqual(Api().Header, expected)
    """

if __name__ == "__main__":
    unittest.main()
