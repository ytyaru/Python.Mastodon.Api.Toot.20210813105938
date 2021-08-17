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
#from test.support import captured_stdout
from unittest.mock import MagicMock, patch, mock_open
import copy
from collections import namedtuple
from string import Template
class TestMediaCli(unittest.TestCase):
    def setUp(self):
        parent = os.path.join(os.path.dirname(__file__), '../src')
        name = 'toot.py'
        path = os.path.abspath(os.path.join(parent, name))
        version = '0.0.1'
        Target = namedtuple('Target', 'name path version')
        self.target = Target(name, path, version)
    def test_run_zero_pos_args(self):
        sys.argv.clear()
        sys.argv.append(self.target)
        with self.assertRaises(SystemExit) as exit:
            mock_lib = MagicMock()
            with patch('media.App.Help', return_value=mock_lib):
                media.Cli().run()
                mock_lib.assert_called_once()
        self.assertEqual(exit.exception.code, 0)
    def test_run_subcommands(self):
        test_cases = {
            'media.App.Version': ['-v', 'v', 'version'],
            'media.App.Help': ['-h', 'h', 'help'],
            'media.App.Author': ['a', 'author'],
            'media.App.Since': ['s', 'since'],
            'media.App.Copyright': ['c', 'copyright'],
            'media.App.License': ['l', 'license'],
            'media.App.Url': ['u', 'url'],
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
                            media.Cli().run()
                            mock_lib.assert_called_once()
                    self.assertEqual(exit.exception.code, 0)
    def test_run_media(self):
        sys.argv.clear()
        sys.argv.append(self.target)
        sys.argv.append('test.png')
        with self.assertRaises(SystemExit) as exit:
            mock_lib = MagicMock()
            with patch('media.App.media', return_value=mock_lib):
                media.Cli().run()
                mock_lib.assert_called_once()
        self.assertEqual(exit.exception.code, 0)

    """
    def test_run_version(self):
        for arg in ['-v', 'v', 'version']:
            with self.subTest(arg=arg):
                sys.argv.clear()
                sys.argv.append(self.target)
                sys.argv.append(arg)
                with self.assertRaises(SystemExit) as exit:
                    mock_lib = MagicMock()
                    with patch('media.App.version', return_value=mock_lib):
                        media.Cli().run()
                        mock_lib.assert_called_once()
                self.assertEqual(exit.exception.code, 0)
    def test_run_help(self):
        for arg in ['-h', 'h', 'help']:
            with self.subTest(arg=arg):
                sys.argv.clear()
                sys.argv.append(self.target)
                sys.argv.append(arg)
                with self.assertRaises(SystemExit) as exit:
                    mock_lib = MagicMock()
                    with patch('media.App.help', return_value=mock_lib):
                        media.Cli().run()
                        mock_lib.assert_called_once()
                self.assertEqual(exit.exception.code, 0)
    def test_run_license(self):
        for arg in ['l', 'license']:
            with self.subTest(arg=arg):
                sys.argv.clear()
                sys.argv.append(self.target)
                sys.argv.append(arg)
                with self.assertRaises(SystemExit) as exit:
                    mock_lib = MagicMock()
                    with patch('media.App.license', return_value=mock_lib):
                        media.Cli().run()
                        mock_lib.assert_called_once()
                self.assertEqual(exit.exception.code, 0)
    def test_run_author(self):
        for arg in ['a', 'author']:
            with self.subTest(arg=arg):
                sys.argv.clear()
                sys.argv.append(self.target)
                sys.argv.append(arg)
                with self.assertRaises(SystemExit) as exit:
                    mock_lib = MagicMock()
                    with patch('media.App.author', return_value=mock_lib):
                        media.Cli().run()
                        mock_lib.assert_called_once()
                self.assertEqual(exit.exception.code, 0)
    def test_run_url(self):
        for arg in ['u', 'url']:
            with self.subTest(arg=arg):
                sys.argv.clear()
                sys.argv.append(self.target)
                sys.argv.append(arg)
                with self.assertRaises(SystemExit) as exit:
                    mock_lib = MagicMock()
                    with patch('media.App.url', return_value=mock_lib):
                        media.Cli().run()
                        mock_lib.assert_called_once()
                self.assertEqual(exit.exception.code, 0)
    """

if __name__ == "__main__":
    unittest.main()
