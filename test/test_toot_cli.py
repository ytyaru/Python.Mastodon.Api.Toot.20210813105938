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
from test.support import captured_stdout
from unittest.mock import MagicMock, patch, mock_open
import copy

class TestTootCli(unittest.TestCase):
    def test_run(self):
        this = 'toot.py'
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
                sys.argv.append('-h')
                toot.Cli().run()
                result = stdout.getvalue()
                self.assertEqual(result, expected)
        self.assertEqual(exit.exception.code, 0)

if __name__ == "__main__":
    unittest.main()
