#!/usr/bin/env python3
# coding: utf8
import requests
import os, sys, argparse, json, urllib.parse
from string import Template
from lib import exept_null, Path, FileReader, FileWriter, Authenticator, Api, Command
class Toot(Api):
    @property
    def ApiUrl(self): return urllib.parse.urljoin(self.BaseUrl, 'api/v1/statuses')
    def toot(self, text):
        data = {}
        data['status'] = text
        data['media_ids'] = []
        data['poll'] = {'options':[], 'expires_in':0}
        print(self.Header, file=sys.stderr)
        print(data, file=sys.stderr)
        res = requests.post(self.ApiUrl, headers=self.Header, data=data)
        print(res.status_code, file=sys.stderr)
        print(res.headers, file=sys.stderr)
        print(res.text, file=sys.stderr)
        return res.json()
class App(Command):
    def toot(self, content): return json.dumps(Toot().toot(content))
"""
class App:
    @classmethod
    def version(self): return '0.0.1'
    @classmethod
    def help(self):
        t = Template(FileReader.text(Path.here('help/toot.txt')))
        return t.substitute(this=Path.name(__file__), version=self.version())
    @classmethod
    def toot(self, content): return json.dumps(Toot().toot(content))
"""
class Cli:
    def __cmd(self, text):
        print(text)
        sys.exit(0)
    def __sub_cmd(self, arg, candidate, text):
        if arg in candidate: self.__cmd(text)
    def __get_content(self):
        if 1 < len(sys.argv): return '\n'.join(sys.argv[1:])
        else: return sys.stdin.read().rstrip('\n')
    def __parse(self):
        if 1 == len(sys.argv): self.__cmd(App().Help)
        elif 1 < len(sys.argv):
            from collections import namedtuple
            SubCmd = namedtuple('SubCmd' , 'candidate text')
            candidates = [
                SubCmd(['-h', 'h', 'help'], App().Help),
                SubCmd(['-v', 'v', 'version'], App().Version),
                SubCmd(['u', 'url'], App().Url),
                SubCmd(['a', 'author'], App().Author['name']),
                SubCmd(['s', 'since'], App().Since.isoformat()),
                SubCmd(['c', 'copyright'], App().Copyright),
                SubCmd(['l', 'license'], App().License['name']),
            ]
            for cmd in candidates: self.__sub_cmd(sys.argv[1], cmd.candidate, cmd.text)
        self.__cmd(App().toot(self.__get_content()))
    def run(self): self.__parse()
    """
    def __parse(self):
        if 1 < len(sys.argv):
            if   '-h' == sys.argv[1]: self.__cmd(App().Help)
            elif '-v' == sys.argv[1]: self.__cmd(App().Version)
        self.__cmd(App().toot(self.__get_content()))
    """

if __name__ == "__main__":
    Cli().run()
