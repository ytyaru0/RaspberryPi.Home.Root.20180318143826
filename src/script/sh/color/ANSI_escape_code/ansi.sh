# https://en.wikipedia.org/wiki/ANSI_escape_code
declare -A ESC_S;
# ESCape Sequences
ESC_S=(
    ["CSI"]="\033["
)
# Select Graphic Rendition
# $1 SGR_P()
function SGR () {
    echo "${ESC_S['CSI']}$1m"
}
function SGR_RESET () {
    echo `SGR 0` # \033[0m
}
# SGR Parameters
# 引数を;区切にする
# $1..$9 = 0..107  https://en.wikipedia.org/wiki/ANSI_escape_code
#function Array () {
function SGR_P () {
    for x in "$@"
    do
        local ret="$ret$x;"
    done
    local ret=`echo $ret | sed -e 's/;$//'`
    echo $ret
}

