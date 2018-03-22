# $1: filepath
# $2: section
[ $# -lt 2 ] && { echo "起動引数エラー。INIファイルパス、セクション名の2つが必要です。"; exit 1; }
INI_FILE=$1
INI_SECTION=$2

eval `sed -e 's/[[:space:]]*\=[[:space:]]*/=/g' \
    -e 's/;.*$//' \
    -e 's/[[:space:]]*$//' \
    -e 's/^[[:space:]]*//' \
    -e "s/^\(.*\)=\([^\"']*\)$/\1=\"\2\"/" \
   < $INI_FILE \
    | sed -n -e "/^\[$INI_SECTION\]/,/^\s*\[/{/^[^;].*\=.*/p;}"`
