#!/usr/bin/env python3
# coding: utf8
#import requests
#import os, sys, argparse, json, urllib.parse, datetime
#from string import Template
#from abc import ABCMeta, abstractmethod
#import mimetypes
import os, sys
# 親ディレクトリをパスに追加する
#sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
#from lib import exept_null, Path, FileReader, FileWriter, Authenticator, Api
#import media
#import unittest
from unittest import TestLoader
from unittest import TextTestRunner
#from test.support import captured_stdout
#from unittest.mock import MagicMock, patch, mock_open
#import copy
#from collections import namedtuple
#from string import Template

if __name__ == '__main__':
    TextTestRunner().run(TestLoader().discover(os.path.abspath(os.path.dirname(__file__))))

