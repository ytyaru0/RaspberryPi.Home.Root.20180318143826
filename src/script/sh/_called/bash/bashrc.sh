# 時刻同期できない問題: .bash_profileだとログイン後に自動実行されるが時刻同期されず。一時ファイルだけが作成されて以降実行されなくなってしまう。
. "$HOME/root/script/sh/_lib/env.sh"
ExportPath "$HOME/root/tool" "$HOME/root/script/sh/_command"
. ~/root/script/sh/mkdir_work.sh
~/root/script/sh/call_settime.sh
. ~/root/script/sh/pyenv.sh
. ~/root/script/sh/py_venv.sh
. ~/root/script/sh/node_module.sh

# 渡されたパスのうち最初に存在したファイルをsourceコマンドで実行する
any_source () { for s in "$@"; do [ -f "$s" ] && { . "$s"; return; }; done }

# ユーザパス設定読込
any_source "/tmp/work/RaspberryPi.Home.Root.20180318143826/src/_meta/path/sh/paths.sh" "${HOME}/root/_meta/path/sh/paths.sh"
# iniファイルからshを作成するには以下コマンド実行。
#python3 ${HOME}/root/_meta/path/IniToSh.py

# コマンドの引数補完セット
any_source "/tmp/work/RaspberryPi.Home.Root.20180318143826/src/_meta/command/do/setup_complete_candidate_do.sh" "${HOME}/root/_meta/command/do/setup_complete_candidate_do.sh"

any_source "/tmp/work/RaspberryPi.Home.Root.20180318143826/src/_meta/command/pj/setup_complete_candidate_pj.sh" "${HOME}/root/_meta/command/do/setup_complete_candidate_pj.sh"
