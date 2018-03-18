# このソフトウェアについて

日常スクリプト。やってみる体系の実装。

日々実装予定。RaspberryPi3 の`$HOME/root/`配下に配置。

# 概要

アウトプット自動化スクリプト。.shファイルを実行することで動く。一部の複雑な処理は.shから.pyを呼びだす形で実装。

# 使い方

1. ターミナルにて`bash -l`
1. `.bash_profile`が呼び出される
1. 環境変数PATHに追加
1. `$ SS`, `$ push`などのコマンドが使用できる

# メモ

* [既知の問題](memo/既知の問題.md)
* [できたらいいな](memo/できたらいいな.md)

# 開発環境

* [Raspberry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 3 Model B
    * [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) GNU/Linux 8.0 (jessie)
        * bash 4.3.30
        * [pyenv](http://ytyaru.hatenablog.com/entry/2019/01/06/000000)
            * Python 3.6.4

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

