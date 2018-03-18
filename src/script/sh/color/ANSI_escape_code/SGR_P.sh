# https://en.wikipedia.org/wiki/ANSI_escape_code
declare -A SGR_P;
SGR_P=(
    ["Reset"]="0"
    ["Bold"]="1"
    ["Underline"]="4"
    ["Reverse"]="7"
)
# SGR_P関数は ansi.sh に定義がある . ./ansi.sh
# $1=0..256
function Color8 () {
    echo `SGR_P 38 5 $1`
}
# $1=0..256
function BackgroundColor8 () {
    echo `SGR_P 48 5 $1`
}
# $1..$3 = R,G,B = 0..255 (8bit)
function Color24 () {
    echo `SGR_P 38 2 $1 $2 $3`
}
# $1..$3 = R,G,B = 0..255 (8bit)
function BackgroundColor24 () {
    echo `SGR_P 48 2 $1 $2 $3`
}
