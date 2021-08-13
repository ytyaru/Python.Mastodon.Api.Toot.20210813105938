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
from unittest.mock import MagicMock
import copy
class TestPath(unittest.TestCase):
    def test_current(self):
        path = 'a.txt'
        self.assertEqual(Path.current(path), 
                        os.path.expandvars(os.path.expanduser(os.path.join(os.getcwd(), path))))
    def test_here(self):
        path = 'a.txt'
        parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        parent = os.path.join(parent, 'src')
        expected = os.path.join(parent, path)
        expected = os.path.expandvars(os.path.expanduser(expected))
        self.assertEqual(Path.here(path), expected)
    def test_name(self):
        path = '/tmp/a.txt'
        self.assertEqual(Path.name(path), os.path.basename(path))
    def test_this_name(self):
        path = '/tmp/a.txt'
        self.assertEqual(Path.this_name(), 'lib.py')

if __name__ == "__main__":
    unittest.main()
