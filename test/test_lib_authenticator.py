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
class TestAuthenticator(unittest.TestCase):
    def test_token(self):
        test_data = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        mock_io = mock_open(read_data=test_data)
        with patch('builtins.open', mock_io):
            actual = Authenticator().Token
            parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            parent = os.path.join(parent, 'src')
            path = os.path.join(parent, 'token.txt')
            path = os.path.expandvars(os.path.expanduser(path))
            mock_io.assert_called_once_with(path, mode='r', encoding='utf-8')
            self.assertEqual(actual, test_data)
    @patch("builtins.open", MagicMock(side_effect=Exception()))
    def test_token_except(self):
        with self.assertRaises(Exception, msg='token.txtがありません。マストドンのインスタンスサーバでアカウントを作り、アプリを作って、アクセストークンを取得し、その値をtoken.txtに書いて保存してください。'):
            Authenticator().Token

if __name__ == "__main__":
    unittest.main()
