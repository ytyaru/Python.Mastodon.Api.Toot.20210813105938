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
class TestFileReader(unittest.TestCase):
    def test_text(self):
        test_data = 'トゥート本文。\n#mastodon #api'
        mock_io = mock_open(read_data=test_data)
        with patch('builtins.open', mock_io):
            actual = FileReader.text('/tmp/dummy.txt')
            mock_io.assert_called_once_with('/tmp/dummy.txt', mode='r', encoding='utf-8')
            self.assertEqual(actual, test_data)
    def test_json(self):
        test_data = '{"id": "1234"}'
        mock_io = mock_open(read_data=test_data)
        with patch('builtins.open', mock_io):
            actual = FileReader.json('/tmp/dummy.json')
            mock_io.assert_called_once_with('/tmp/dummy.json', mode='r', encoding='utf-8')
            self.assertEqual(actual, json.loads(test_data))

if __name__ == "__main__":
    unittest.main()
