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
class TestFileWriter(unittest.TestCase):
    def test_text(self):
        test_data = 'トゥート本文。\n#mastodon #api'
        mock_io = mock_open()
        with patch('builtins.open', mock_io):
            actual = FileWriter.text('/tmp/dummy.txt', test_data)
            mock_io.assert_called_once_with('/tmp/dummy.txt', mode='w', encoding='utf-8')
    def test_json(self):
        test_data = '{"id": "1234"}'
        mock_io = mock_open()
        with patch('builtins.open', mock_io):
            actual = FileWriter.json('/tmp/dummy.json', test_data)
            mock_io.assert_called_once_with('/tmp/dummy.json', mode='w', encoding='utf-8')

if __name__ == "__main__":
    unittest.main()
