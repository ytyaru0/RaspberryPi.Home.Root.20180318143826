# 時刻同期できない問題: .bash_profileだとログイン後に自動実行されるが時刻同期されず。一時ファイルだけが作成されて以降実行されなくなってしまう。
. "$HOME/root/script/sh/_lib/env.sh"
ExportPath "$HOME/root/tool" "$HOME/root/script/sh/_command"
. ~/root/script/sh/mkdir_work.sh
~/root/script/sh/call_settime.sh
. ~/root/script/sh/pyenv.sh
. ~/root/script/sh/py_venv.sh
