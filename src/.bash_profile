#!/bin/sh
#export PATH="$PATH:/home/pi/root/tool"
export PATH="$PATH:$HOME/root/tool:$HOME/root/script/sh/_command"
rm -f /tmp/work/.meta/.settime 
~/root/script/sh/call_settime.sh
. ~/root/script/sh/mkdir_work.sh
. ~/root/script/sh/pyenv.sh
. ~/root/script/sh/py_venv.sh

