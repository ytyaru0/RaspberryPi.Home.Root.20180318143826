# アウトプット系コマンド

## y

```sh
$ y {lang} {context}
```

* `0.py`など単一ファイル作成
* 最小限のテンプレ
* 順序付ファイル名

さらに以下のことができると便利。

* 最新は一つ前のコピーファイルとする
* `/tmp/work/y/`配下に必ず配置する
* `$ cd /tmp/work/y/`
* ターミナルのタブ生成
    * エディタ起動: `$ vim /tmp/work/y/{作成ファイル名}`
    * 初回実行: `$ python {作成ファイルパス}`

## pj

```sh
$ pj {lang} {context}
```

* 複数ファイル作成
* `src/`, `test/`などディレクトリ構造があり相対パス関係にあるコード
* `/tmp/work/pj/`配下に作る

`y`コマンドの複雑な構成版。

なお、`/tmp/work/y/`配下で`$ pj`とするとプロジェクト化する。

1. `/tmp/work/pj/{lang}.{datetime}/`ディレクトリ生成
1. `./src/`生成する
1. 2に`/tmp/work/y/`配下コードをコピーする
1. `/tmp/work/y/`配下コードを削除する

## repo

```sh
$ repo -l {license} {lang} {context}
```

* README, LICENSE, .gitignore 作成
* テンプレ
    * {lang}, {context} を引数にして
        * README.md
    * {license} を引数にして
        * LICENSE
    * {lang}, {context} を引数にして
        * .gitignore

なお、`/tmp/work/pj/*/`ディレクトリ配下で実行すると、READMEなどを作成する。既存なら無視。

