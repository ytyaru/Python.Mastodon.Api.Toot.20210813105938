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
#        DummyReader = copy.deepcopy(FileReader)
#        test_data = 'test-data'
#        DummyReader.text = MagicMock(return_value=test_data) 
#        self.assertEqual(DummyReader.text(), test_data)
        test_data = 'トゥート本文。\n#mastodon #api'
        mock_io = mock_open(read_data=test_data)
        # openは組み込み関数なので、「builtins」を使う
        with patch('builtins.open', mock_io):
            mock_io.assert_called_once_with('/tmp/dummy.txt', mode='r')
            self.assertEqual(FileReader.text('dummy.txt'), ['トゥート本文。\n', '#mastodon #api\n'])
    def test_json(self):
        DummyReader = copy.deepcopy(FileReader)
        test_data = {"id": "1234"}
        DummyReader.json = MagicMock(return_value=test_data) 
        self.assertEqual(DummyReader.json(), test_data)

if __name__ == "__main__":
    unittest.main()
