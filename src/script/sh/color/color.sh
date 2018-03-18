. ~/root/script/sh/color/ANSI_escape_code/ansi.sh
. ~/root/script/sh/color/ANSI_escape_code/SGR_P.sh
# $1: 色ID
Color () {
    . ~/root/script/sh/color/ANSI_escape_code/color_define.sh
    if [ 1 -le $# ]; then
        echo `SGR ${COLORS[$1]}`
    else
        echo `SGR_RESET`
    fi
}
# $1: 色ID
Color8 () {
    . ~/root/script/sh/color/ANSI_escape_code/color8_define.sh
    if [ 1 -le $# ]; then
        echo `SGR $(Color8 ${COLORS[$cid]})`
    else
        echo `SGR_RESET`
    fi
}

