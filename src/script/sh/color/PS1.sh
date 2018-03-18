# ----------------------------------------------------
# 環境変数PS1をかっこよくする
# 表示例
#   (python venv) (chroot) user@host:cd $ 
# 引数
#   $1: python -venv の仮想環境名
# 参考
#   https://qiita.com/HMMNRST/items/d8fe7b3c528f447d68a6
#   https://en.wikipedia.org/wiki/ANSI_escape_code
# ----------------------------------------------------
# Select Graphic Rendition
function SGR () {
    echo "\[\033[$1m\]"
}
# 引数を;区切にする
function Array () {
    for x in "$@"
    do
        local ret="$ret$x;"
    done
    local ret=`echo $ret | sed -e 's/;$//'`
    echo $ret
}
venv_name=$1
venv_name=${venv_name:+$venv_name }
#venv_name=${venv_name:+($venv_name) }
user_name="\u"
host_name="\h"
work_dir="\w"
chroot=`${debian_chroot:+($debian_chroot) }`

#SCRIPT_DIR=$(cd $(dirname $0); pwd)
#echo $SCRIPT_DIR

RESET=`SGR 00` # RESET, NORMAL, OFF
# 呼出元のパス次第で相対パスが狂う。PS1.shのパスを取得できない。呼出元のパスしか取れない。
#. ./ANSI_escape_code/color_define.sh
. ~/root/script/sh/color/ANSI_escape_code/color_define.sh
COL_VENV=`SGR ${COLORS["BR"]}`
COL_CHROOT=`SGR ${COLORS["BY"]}`
COL_USERHOST=`SGR ${COLORS["BG"]}`
COL_DIR=`SGR ${COLORS["BB"]}`
# 多彩な色の設定方法↓
#COL_DIR=`SGR $(Array ${SGR_P["Bold"]} ${COLORS["B"]})` # 併用（PARAM + Color）
#. ./ANSI_escape_code/SGR_P.sh
#. ./ANSI_escape_code/color8_define.sh
#COL_DIR=`SGR $(SGR_P 38 5 $(GetColor 5 2 1))` # 6bit color (R,G,Bは0..5の値)
#COL_DIR=`SGR $(SGR_P 38 2 $(GetColor 255 255 255))` # 24bit color (R,G,Bは0..255の値)
#COL_DIR=`SGR $(Color8 ${COLORS["R"]})` # 0..7, 8..15
#COL_DIR=`SGR $(Color8 $(GetColor 5 2 1))` # 6bit color (R,G,Bは0..5の値)
#COL_DIR=`SGR $(Color24 $(GetColor 255 196 108))` # 24bit color (R,G,Bは0..255の値)
#COL_DIR=`SGR $(BackgroundColor8 $(GetColor 5 2 1))` # 6bit color (R,G,Bは0..5の値)
#COL_DIR=`SGR $(BackgroundColor24 $(GetColor 255 196 108))` # 24bit color (R,G,Bは0..255の値)

PS1="${COL_VENV}${venv_name}${COL_CHROOT}${chroot}${COL_USERHOST}${user_name}@${host_name}${RESET}:${COL_DIR}${work_dir} \$${RESET} "

