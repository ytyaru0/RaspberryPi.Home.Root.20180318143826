# https://qiita.com/sayama0402/items/6385b9019f37031eb2b9
# 8bit color (0..255)
#     0..  7: Black,Red,Green,Yellow,Blue,Magenta,Cyan,White
#     8.. 16: Bright + [Black,Red,Green,Yellow,Blue,Magenta,Cyan,White]
#   232..255: GrayScale
#    17..232: 6bit color

# $1, $2, $3 = R,G,B = 0..5 (6bit)
function GetColor() {
    echo `(expr 16 + 36 \* $1 + 6 \* $2 + $3)`
}
function GetStandardColors() {
    echo `seq 0 7`
}
function GetBrightColors() {
    echo `seq 8 15`
}
function GetGrayScale() {
    echo `seq 232 255`
}
declare -A COLORS;
COLORS=(
    ["BLACK"]="0"
    ["R"]="1"
    ["G"]="2"
    ["Y"]="3"
    ["B"]="4"
    ["M"]="5"
    ["C"]="6"
    ["W"]="7"
    ["BBLACK"]="8"
    ["BR"]="9"
    ["BG"]="10"
    ["BY"]="11"
    ["BB"]="12"
    ["BM"]="13"
    ["BC"]="14"
    ["BW"]="15"
)
