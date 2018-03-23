# 時刻同期できない問題: .bash_profileだとログイン後に自動実行されるが時刻同期されず。一時ファイルだけが作成されて以降実行されなくなってしまう。
. "$HOME/root/script/sh/_lib/env.sh"
ExportPath "$HOME/root/tool" "$HOME/root/script/sh/_command"
. ~/root/script/sh/mkdir_work.sh
~/root/script/sh/call_settime.sh
. ~/root/script/sh/pyenv.sh
. ~/root/script/sh/py_venv.sh

# ユーザパス設定読込
python3 /tmp/work/RaspberryPi.Home.Root.20180318143826/src/_meta/path/IniToSh.py
. /tmp/work/RaspberryPi.Home.Root.20180318143826/src/_meta/path/sh/paths.sh
#python3 ~/root/_meta/path/IniToSh.py
#. ~/root/_meta/path/sh/paths.sh

# コマンドの引数補完セット
. /tmp/work/Python.TemplateFileMaker.20180314204216/src/setup_complete_candidate_do.sh
#. ~/root/_meta/command/setup_complete_candidate_do.sh

