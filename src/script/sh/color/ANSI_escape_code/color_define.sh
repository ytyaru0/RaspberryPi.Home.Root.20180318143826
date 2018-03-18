# https://en.wikipedia.org/wiki/ANSI_escape_code
# https://qiita.com/sayama0402/items/6385b9019f37031eb2b9
declare -A COLORS;
COLORS=(
    ["BLACK"]="30"
    ["R"]="31"
    ["G"]="32"
    ["Y"]="33"
    ["B"]="34"
    ["M"]="35"
    ["C"]="36"
    ["W"]="37"
    ["BBLACK"]="90"
    ["BR"]="91"
    ["BG"]="92"
    ["BY"]="93"
    ["BB"]="94"
    ["BM"]="95"
    ["BC"]="96"
    ["BW"]="97"
)
# ${COLORS["R"]}
declare -A BG_COLORS;
BG_COLORS=(
    ["BLACK"]="40"
    ["R"]="41"
    ["G"]="42"
    ["Y"]="43"
    ["B"]="44"
    ["M"]="45"
    ["C"]="46"
    ["W"]="47"
    ["BBLACK"]="100"
    ["BR"]="101"
    ["BG"]="102"
    ["BY"]="103"
    ["BB"]="104"
    ["BM"]="105"
    ["BC"]="106"
    ["BW"]="107"
)
# ${BG_COLORS["R"]}
