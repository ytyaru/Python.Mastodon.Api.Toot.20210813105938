# Authenticator

　認証についてはいずれちゃんと実装したい。

## 要素

* Mastodon インスタンス ドメイン名
    * ユーザ名
    * パスワード
        * client_id
        * client_secret
            * access_token

　このうちパスワードはどう管理すべきか。間違ってもリポジトリにアップロードしたくない。最悪、今やっているようにアクセストークンのみでいい。これをサイトで生成するだけ。このツールでは管理しない。

* domain
    * username
        * password
            * client_id
            * client_secret
                * access_token

　以下の2要素からパスワードを返す簡単なスクリプトを作る案。これでアップロードするソースコードにはパスワードのハードコーディングがされない。パスワードを含むデータは指定したパスにTSVファイルで保存する。エンドユーザはそのファイルを管理すればよい。ただし`which pw`とされるとスクリプトのパスが判明する。そこからあっという間にTSVパスもバレる。ログインしないかぎりできない。

```sh
$ pw mstdn.jp ytyaru
password
```
```sh
$ token mstdn.jp ytyaru app_name
token
```

# mstdn.js

## 403エラー

　HTTPヘッダの`User-Agent`を設定しないと403エラーが返された。

```javascript
'User-Agent': 'Mozilla/5.0 (X11; CrOS armv7l 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.187 Safari/537.36',
```

