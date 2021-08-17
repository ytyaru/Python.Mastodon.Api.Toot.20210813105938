#!/usr/bin/env python3
# coding: utf8
import requests
import os, sys, argparse, json, urllib.parse, datetime
from string import Template
import inspect
from collections import namedtuple
def exept_null(f):
    def _wrapper(*args, **kwargs):
        try: return f(*args, **kwargs)
        except: return None
    return _wrapper
class Path:
    @classmethod
    def current(cls, path): # カレントディレクトリからの絶対パス
        return cls.__expand(os.path.join(os.getcwd(), path))
    @classmethod
    def here(cls, path): # このファイルからの絶対パス
        return cls.__expand(os.path.join(os.path.dirname(os.path.abspath(__file__)), path))
    @classmethod
    def name(cls, path): # このファイル名
        return os.path.basename(path)
    @classmethod
    def this_name(cls): # このファイル名
        return os.path.basename(__file__)
    @classmethod
    def __expand(cls, path): # homeを表すチルダや環境変数を展開する
        return os.path.expandvars(os.path.expanduser(path))
class FileReader:
    @classmethod
    @exept_null
    def text(self, path):
        with open(path, mode='r', encoding='utf-8') as f: return f.read().rstrip('\n')
    @classmethod
    def json(self, path):
        with open(path, mode='r', encoding='utf-8') as f: return json.load(f)
class FileWriter:
    @classmethod
    def text(self, path, content):
        with open(path, mode='w', encoding='utf-8') as f: f.write(content)
    @classmethod
    def json(self, path, content):
        with open(path, mode='w', encoding='utf-8') as f: json.dump(content, f)
class Authenticator:
    @property
    def Token(self):
        token = FileReader.text(Path.here('token.txt'))
        if token is None: raise Exception('token.txtがありません。マストドンのインスタンスサーバでアカウントを作り、アプリを作って、アクセストークンを取得し、その値をtoken.txtに書いて保存してください。')
        return token
class Api:
    def __init__(self):
        self.__auth = Authenticator()
    @property
    def Auth(self): return self.__auth
    @property
    def BaseUrl(self):
        candidates = [FileReader.text(Path.here('host.txt')), 'mstdn.jp']
        hosts = [c for c in candidates if c is not None]
        return f'https://{hosts[0]}/'
    @property
    def Header(self):
        return {
            'User-Agent': FileReader.text('user-agent.txt'),
#            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.Auth.Token}',
        }
class Command:
    @property
    def Version(self): return '0.0.1'
    @property
    def Help(self):
        name, ext = os.path.splitext(os.path.basename(inspect.getfile(self.__class__)))
        parent = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(parent, f'help/{name}.txt')
        with open(path, mode='r', encoding='utf-8') as f:
            t = Template(f.read().rstrip('\n'))
            return t.substitute(this=f'{name}{ext}', version=self.Version)
#        t = Template(FileReader.text(Path.here('help/toot.txt')))
#        return t.substitute(this=Path.name(__file__), version=self.version())
    @property
    def Since(self):
        return datetime.datetime(2021, 8, 12, 0, 0, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=9)))
    @property
    def Author(self):
        a = {}
        a['name'] = 'ytyaru'
        a['url'] = f'https://github.com/{a["name"]}'
        return a
    @property
    def Copyright(self): return f'© {self.Since.year} {self.Author["name"]}'
    @property
    def License(self):
        l = {}
        l['name'] = 'MIT'
        l['spdx'] = l['name']
        l['url'] = 'https://opensource.org/licenses/MIT'
        return l
    @property
    def Url(self): return 'https://github.com/ytyaru/Python.Mastodon.Api.Toot.20210812120350'
class SubCmdParser:
    def __init__(self):
        self.__SubCmd = namedtuple('SubCmd' , 'candidate text')
        self.__candidates  = []
    def __cmd(self, text):
        print(text)
        sys.exit(0)
    def __sub_cmd(self, arg, candidate, text):
        if arg in candidate: self.__cmd(text)
    def add(self, candidate, text):
        self.__candidates.append(self.__SubCmd(candidate, text))
    def parse(self):
        for c in self.__candidates:
            self.__sub_cmd(sys.argv[1], c.candidate, c.text)

