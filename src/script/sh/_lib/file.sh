# $1 対象ファイルパス
#GetSize () { echo `wc -c "$1" | awk '{print $1}'`; }
#GetSize () { echo `stat -c %s "$1"`; }
GetSize () { stat -c %s "$1"; }
# $1 必須 対象ファイルパス
# $2 任意 日付の書式
GetLastUpdated () { echo `__GetDate "%y" "$@"`; }
GetLastAccessed () { echo `__GetDate "%x" "$@"`; }
GetPermissionLastChanged () { echo `__GetDate "%z" "$@"`; }
# $1 stat引数(%x,%y,%z) $2 対象ファイルパス, $3 日付の書式
__GetDate () {
    format=`__GetDateFormat "$@"`
    echo `stat -c $1 "$2"  | date -f - "+${format}"`
}
# $1 stat引数(%x,%y,%z) $2 対象ファイルパス, $3 日付の書式
__GetDateFormat () {
    if [ $# -lt 3 ]; then
        echo "%Y-%m-%d %H:%M:%S"
    else
        echo "${3}"
    fi
}
