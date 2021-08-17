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
#from test.support import captured_stdout
from unittest.mock import MagicMock, patch, mock_open
import copy
from collections import namedtuple
class TestTootCli(unittest.TestCase):
    def setUp(self):
        parent = os.path.join(os.path.dirname(__file__), '../src')
        name = 'toot.py'
        path = os.path.abspath(os.path.join(parent, name))
        version = '0.0.1'
        Target = namedtuple('Target', 'name path version')
        self.target = Target(name, path, version)
    def test_run_subcommands(self):
        test_cases = {
            'toot.App.Version': ['-v', 'v', 'version'],
            'toot.App.Help': ['-h', 'h', 'help'],
            'toot.App.Author': ['a', 'author'],
            'toot.App.Since': ['s', 'since'],
            'toot.App.Copyright': ['c', 'copyright'],
            'toot.App.License': ['l', 'license'],
            'toot.App.Url': ['u', 'url'],
        }
        for called_method, args in test_cases.items():
            for arg in args:
                with self.subTest(arg=arg):
                    sys.argv.clear()
                    sys.argv.append(self.target)
                    sys.argv.append(arg)
                    with self.assertRaises(SystemExit) as exit:
                        mock_lib = MagicMock()
                        with patch(called_method, return_value=mock_lib):
                            toot.Cli().run()
                            mock_lib.assert_called_once()
                    self.assertEqual(exit.exception.code, 0)

    def test_run_version(self):
        sys.argv.clear()
        sys.argv.append(self.target.path)
        sys.argv.append('-v')
        with self.assertRaises(SystemExit) as exit:
            mock_lib = MagicMock()
            with patch('toot.App.Version', return_value=mock_lib):
                toot.Cli().run()
                mock_lib.assert_called_once()
        self.assertEqual(exit.exception.code, 0)
    def test_run_help(self):
        sys.argv.clear()
        sys.argv.append(self.target.path)
        sys.argv.append('-h')
        with self.assertRaises(SystemExit) as exit:
            mock_lib = MagicMock()
            with patch('toot.App.Help', return_value=mock_lib):
                toot.Cli().run()
                mock_lib.assert_called_once()
        self.assertEqual(exit.exception.code, 0)
    def test_run_toot(self):
        sys.argv.clear()
        sys.argv.append(self.target.path)
        sys.argv.append('test.png')
        mock_lib = MagicMock()
        with self.assertRaises(SystemExit) as exit:
            with patch('toot.App.toot', return_value=mock_lib):
                toot.Cli().run()
                mock_lib.assert_called_once()
        self.assertEqual(exit.exception.code, 0)

if __name__ == "__main__":
    unittest.main()
