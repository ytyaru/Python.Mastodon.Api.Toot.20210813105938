[ja](./README.ja.md)

# Mastodon.Api.Toot

Toot with the Mastodon API.

# DEMO

* [demo](https://ytyaru.github.io/Python.Mastodon.Api.Toot.20210813105938/)

![img](https://github.com/ytyaru/Python.Mastodon.Api.Toot.20210813105938/blob/master/doc/0.png?raw=true)

# Features

* sales point

# Requirement

* <time datetime="2021-08-13T10:59:30+0900">2021-08-13</time>
* [Raspbierry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 4 Model B Rev 1.2
* [Raspberry Pi OS](https://ja.wikipedia.org/wiki/Raspbian) buster 10.0 2020-08-20 <small>[setup](http://ytyaru.hatenablog.com/entry/2020/10/06/111111)</small>
* bash 5.0.3(1)-release
* Python 2.7.16
* Python 3.7.3
* [pyxel][] 1.3.1

[pyxel]:https://github.com/kitao/pyxel

```sh
$ uname -a
Linux raspberrypi 5.10.52-v7l+ #1441 SMP Tue Aug 3 18:11:56 BST 2021 armv7l GNU/Linux
```

# Installation

```sh
pip3 install -r requirements.txt
```

# Usage

```sh
git clone https://github.com/ytyaru/Python.Mastodon.Api.Toot.20210813105938
cd Python.Mastodon.Api.Toot.20210813105938/src
./run.py
```

## Prepare an access token

1. Create an account on any instance of Mastodon
1. Create a `app` from the `development` of the menu
1. Generate an access token

`` `sh
git clone https://github.com/ytyaru/Python.Mastodon.Api.Toot.20210813105938
cd Python.Mastodon.Api.Toot.20210813105938/src
echo "$GENERATED_ACCESS_TOKEN" > token.txt
`` ```

## Toot

```sh
./toot.py 'Toot body.'
```
```sh
echo -e 'Toot body.\n#hashtag'| ./toot.py
```

# Author

ytyaru

* [![github](http://www.google.com/s2/favicons?domain=github.com)](https://github.com/ytyaru "github")
* [![hatena](http://www.google.com/s2/favicons?domain=www.hatena.ne.jp)](http://ytyaru.hatenablog.com/ytyaru "hatena")
* [![mastodon](http://www.google.com/s2/favicons?domain=mstdn.jp)](https://mstdn.jp/web/accounts/233143 "mastdon")

# License

This software is CC0 licensed.

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.en)

