. ~/root/script/sh/_userlib/py_venv.sh ranger
#. /tmp/work/RaspberryPi.Home.Root.20180318143826/src/script/sh/_userlib/py_venv.sh ranger

# :r でpythonファイル実行させたとき、一瞬で表示が消えてしまう問題を解決したかったが、できなかった。
# http://malkalech.com/ranger_filer#less
#ranger
LESS="$LESS -+F -+X" ranger
