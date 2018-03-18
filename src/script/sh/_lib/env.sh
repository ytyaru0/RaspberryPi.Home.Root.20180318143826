# 環境変数の追加（重複せずに）
# $1.. $PATHに追加したいパス
ExportPath () {
    for target in "$@"; do
        [[ "$PATH" =~ ":${target}" ]] || [[ "$PATH" =~ "${target}:" ]] && continue
        export PATH="${PATH}:${target}"
    done
}
#echo "start 環境変数: $PATH"
#ExportPath /tmp/work/.meta /tmp/work/.meta "/tmp/work/A あ.txt"
#echo "end   環境変数: $PATH"
