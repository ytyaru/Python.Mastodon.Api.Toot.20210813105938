[en](./README.md)

# Mastodon.Api.Toot

　Mastodon API で Toot する。

# デモ

* [demo](https://ytyaru.github.io/Python.Mastodon.Api.Toot.20210813105938/)

![img](https://github.com/ytyaru/Python.Mastodon.Api.Toot.20210813105938/blob/master/doc/0.png?raw=true)

# 特徴

* セールスポイント

# 開発環境

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

# インストール

```sh
pip3 install -r requirements.txt
```

# 使い方

## アクセストークンを用意する

1. Mastodonの任意インスタンスでアカウントをつくる
1. メニューの`開発`から`アプリ`をつくる
1. アクセストークンを生成する

```sh
git clone https://github.com/ytyaru/Python.Mastodon.Api.Toot.20210813105938
cd Python.Mastodon.Api.Toot.20210813105938/src
echo '＜生成したアクセストークン＞' > token.txt
```

## Tootする

```sh
./toot.py 'Toot本文。'
```
```sh
echo -e 'Toot本文。\n#hashtag' | ./toot.py
```

# 著者

　ytyaru

* [![github](http://www.google.com/s2/favicons?domain=github.com)](https://github.com/ytyaru "github")
* [![hatena](http://www.google.com/s2/favicons?domain=www.hatena.ne.jp)](http://ytyaru.hatenablog.com/ytyaru "hatena")
* [![mastodon](http://www.google.com/s2/favicons?domain=mstdn.jp)](https://mstdn.jp/web/accounts/233143 "mastdon")

# ライセンス

　このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

