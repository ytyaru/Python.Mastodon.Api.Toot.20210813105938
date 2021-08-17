#!/usr/bin/env python3
# coding: utf8
import requests
import os, sys, argparse, json, urllib.parse, datetime
from string import Template
from lib import exept_null, Path, FileReader, FileWriter, Authenticator, Api, Command, SubCmdParser
from abc import ABCMeta, abstractmethod
import mimetypes
import toml
import copy
# https://docs.joinmastodon.org/ja/user/posting/#attachments
class Limit(metaclass=ABCMeta):
    @abstractmethod
    def num(self): pass
    @abstractmethod
    def size(self): pass
    @abstractmethod
    def formats(self): pass
class ImageLimit(Limit):
    def num(self): return 4
    def size(self): return 8,000,000
    def formats(self): return ['png', 'gif', 'jpg', 'jpeg']
    def git_animation(self): return 'mp4'
class MovieLimit(Limit):
    def num(self): return 1
    def size(self): return 40,000,000
    def formats(self): return ['mp4', 'm4v', 'mov', 'webm']
    def bit_rate(self): return 1300
    def frame_rate(self): return 60
class AudioLimit(Limit):
    def num(self): return 1
    def size(self): return 40,000,000
    def formats(self): return ['mp3', 'ogg', 'wav', 'flac', 'opus', 'aac', 'm4a', '3gp']
# https://docs.joinmastodon.org/methods/statuses/media/
class Media(Api):
    @property
    def ApiUrl(self): return urllib.parse.urljoin(self.BaseUrl, 'api/v1/media')
    def media(self, path, thumbnail=None, description=None, focus=None):
        files = {}
        files['file'] = self.__file_tuple(path)
        if thumbnail is not None: files['thumbnail'] = self.__file_tuple(thumbnail)
        params = {}
        if description is not None: params['description'] = description
        if focus is not None: params['focus'] = focus
        print(self.Header, file=sys.stderr)
        print(params, file=sys.stderr)
        print(files, file=sys.stderr)
        res = requests.post(self.ApiUrl, headers=self.Header, files=files, params=params)
        print(res.status_code, file=sys.stderr)
        print(res.headers, file=sys.stderr)
        print(res.text, file=sys.stderr)
        return res.json()
    def __file_tuple(self, path):
#        return (path, open(path,'rb').read(), mimetypes.guess_type(path)[0])
        with open(path, 'rb') as f: return (path, f.read(), mimetypes.guess_type(path)[0])
class App(Command):
    def media(self, *args, **kwargs): return json.dumps(Media().media(*args, **kwargs))
"""
class App:
    @classmethod
    def version(self): return '0.0.1'
#    def version(self): return FileReader.text(Path.here('version-media.txt'))
    @classmethod
    def help(self):
        t = Template(FileReader.text(Path.here('help/media.txt')))
        return t.substitute(this=Path.name(__file__), version=self.version())
    @classmethod
    def since(self):
        return datetime.datetime(2021, 8, 12, 0, 0, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=9)))
    @classmethod
    def author(self):
        a = {}
        a['name'] = 'ytyaru'
        a['url'] = f'https://github.com/{a["name"]}'
        return a
    @classmethod
    def copyright(self): return f'© {App.since().year} {App.author()["name"]}'
    @classmethod
    def license(self):
        l = {}
        l['name'] = 'MIT'
        l['spdx'] = l['name']
        l['url'] = 'https://opensource.org/licenses/MIT'
        return l
    @classmethod
    def url(self): return 'https://github.com/ytyaru/Python.Mastodon.Api.Toot.20210812120350'
    @classmethod
    def media(self, *args, **kwargs): return json.dumps(Media().media(*args, **kwargs))
"""
class ArgParser:
    def parse(self):
        args = []
        kwargs = {}
        optionals = {'-t': 'thumbnail',
                     '-d': 'description',
                     '-f': 'focus'}
        if 2 == len(sys.argv): args.append(sys.argv[1])
        else:
            argv = copy.deepcopy(sys.argv[1:])
            for i, arg in enumerate(argv):
                opt = list(filter(lambda o: o == arg, optionals))
                if 0 == len(opt): continue
                opt = opt[0]
                if (i+1 < len(argv) - 1): raise Exception(f'引数不足。オプション引数{opt}には値が必要です。')
                kwargs.append(optionals[opt], argv[i+1])
            args.append(argv[0] if 0 == len(list(filter(lambda o: o == argv[0], optionals))) else argv[-1])
#        if not os.path.isfile(args[0]): raise Exception(f'引数不正。指定したファイルは存在しません。{args[0]}')
        return args, kwargs
class Cli:
    def __cmd(self, text):
        print(text)
        sys.exit(0)
    def __get_content(self): return ArgParser().parse()
    def __parse(self):
        if 1 == len(sys.argv): self.__cmd(App().Help)
        elif 1 < len(sys.argv):
            parser = SubCmdParser()
            parser.add(['-h', 'h', 'help'], App().Help)
            parser.add(['-v', 'v', 'version'], App().Version)
            parser.add(['u', 'url'], App().Url)
            parser.add(['a', 'author'], App().Author['name'])
            parser.add(['s', 'since'], App().Since.isoformat())
            parser.add(['c', 'copyright'], App().Copyright)
            parser.add(['l', 'license'], App().License['name'])
            parser.parse()
        self.__cmd(App().media(self.__get_content()))
    def run(self): self.__parse()
if __name__ == "__main__":
    Cli().run()
