#!/bin/bash
# $1: 実行したいshファイルフルパス（"~/settime.sh"なら"/tmp/work/.meta/.settime"ファイルを作成する）
# settime.sh は6秒くらいかかるので1回だけ実行するようにしたい。
# 1回実行したら一時ファイルを作る。それが存在したら実行しない。
tmpfilename=`basename ${1}`
without_ext=${tmpfilename%.*}
tmpfile=/tmp/work/.meta/.${without_ext}
#echo $tmpfile
if [ ! -f $tmpfile ]; then
    . "${1}"
    mkdir -p `dirname $tmpfile`
    touch $tmpfile
fi
unset tmpfile
unset without_ext
unset tmpfilename


