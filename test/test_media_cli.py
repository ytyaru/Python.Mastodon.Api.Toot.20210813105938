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
from test.support import captured_stdout
from unittest.mock import MagicMock, patch, mock_open
import copy

class TestTootCli(unittest.TestCase):
    def setUp(self):
        parent = os.path.join(os.path.dirname(__file__), '../src')
        self.target = os.path.abspath(os.path.join(parent, 'media.py'))
    def test_run_version(self):
        this = 'media.py'
        version = '0.0.1'
        with self.assertRaises(SystemExit) as exit:
            with captured_stdout() as stdout:
                sys.argv.clear()
                sys.argv.append(self.target)
                sys.argv.append('-v')
                media.Cli().run()
                result = stdout.getvalue()
                self.assertEqual(result, expected)
        self.assertEqual(exit.exception.code, 0)
    def test_run_help(self):
        this = 'media.py'
        version = '0.0.1'
        expected = '''MastodonのAPIを叩いてTootする。	{version}
Usage:
  {this} [-h] [-v] [MESSAGE ...]
Documents:
  https://docs.joinmastodon.org/methods/statuses/
Examples:
  {this} MSG1 MSG2 MSG3
  echo -e 'MSG1\nMSG2\nMSG3' | {this}'''
        with self.assertRaises(SystemExit) as exit:
            with captured_stdout() as stdout:
                sys.argv.clear()
                sys.argv.append(self.target)
                sys.argv.append('-h')
                media.Cli().run()
                result = stdout.getvalue()
                self.assertEqual(result, expected)
        self.assertEqual(exit.exception.code, 0)
    def test_run_media(self):
        mock_lib = MagicMock()
        with self.assertRaises(SystemExit) as exit:
            with patch('media.App.media', return_value=mock_lib):
                sys.argv.clear()
                sys.argv.append(self.target)
                sys.argv.append('test.png')
                self.assertEqual(sys.argv[1], 'test.png')
                media.Cli().run()
                mock_lib.assert_called_once()
        self.assertEqual(exit.exception.code, 0)

if __name__ == "__main__":
    unittest.main()
