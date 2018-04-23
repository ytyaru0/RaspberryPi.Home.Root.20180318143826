function GetExt() {
    local filename=`GetFilename ${1}`
    echo ${filename##*.}
}
function GetFilename() {
    echo `basename ${1}`
}
function GetParent() {
    echo `dirname ${1}`
}
function GetChildren() {
    echo `ls -1 ${1}`
}
function GetFilenameWithoutExt() {
    local filename=`GetFilename ${1}`
    echo ${filename%.*}
    # echo ${$(GetFilename ${1})%.*} # 誤った代入です
}
function Join() {
    dirname=`echo $1 | sed -E 's/\/*$//g'`
    basename=`echo $2 | sed -E 's/^\/*//g'`
    echo "$dirname/$basename"
}
function GetHiddenFilename() {
    echo "."`GetFilenameWithoutExt ${1}`
}
# sed: https://bi.biopapyrus.jp/os/linux/sed.html
# 文字列操作: https://qiita.com/sotarok/items/9f2ccffc23bd36534e2e
GetChildrenDirnames() {
    local target=$1
    [ ! -d "$target" ] && { echo "存在するディレクトリを指定してくしてください。: ${target}"; return; }
    for dir in `\find "${target}" -maxdepth 1 -type d | sort`; do
        local dname=`basename $dir`
        [ "$dname" == `basename $target` ] && continue
        echo $dname
    done
}
