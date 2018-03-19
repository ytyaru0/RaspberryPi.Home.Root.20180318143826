# 目的: ユーザディレクトリのパス管理。パスを変更するとき、ここを変更することで他のシェルも一括変更できる
declare -A Path;
Path=(
    ["Work"]="/tmp/work/"
    ["WorkMeta"]="/tmp/work/.meta/"
    ["WorkFlowDo"]="/tmp/work/flow/do/"
    ["WorkFlowPj"]="/tmp/work/flow/pj/"
    ["WorkFlowRepo"]="/tmp/work/flow/repo/"
    ["SS"]="/tmp/work/SS/"
    ["Root"]="$HOME/root/"
    ["ShellScript"]="$HOME/root/script/sh/"
)
# for p in ${!Path[@]}; do { printf "%12s" "$p"; echo ": ${Path[$p]}"; } done

# 用途: 作業ファイル一式を配置する。（RAMディスクにする。Raspbianにおいて書込によるSDカード劣化防止対策）
GetWorkDir () { echo "/tmp/work/"; }
# 用途: settime.sh用一時ファイル配置など。
GetWorkMetaDir () { echo `GetWorkDir`".meta/"; }
# 用途: doコマンド用ディレクトリ。
GetWorkFlowDoDir () { echo `GetWorkDir`"flow/do/"; }
# 用途: pjコマンド用ディレクトリ。
GetWorkFlowPjDir () { echo `GetWorkDir`"flow/pj/"; }
# 用途: repoコマンド用ディレクトリ。
GetWorkFlowRepoDir () { echo `GetWorkDir`"flow/repo/"; }
# 用途: スクリーンショット画像を配置する
GetScreenShotDir () { echo `GetWorkDir`"SS/"; }
# 用途: ユーザが管理するディレクトリのルート
GetRootDir () { echo "$HOME/root/"; }
GetShellScriptDir () { echo `GetRootDir`"script/sh/"; }

# $1: ファイルパス
# /tmp/work/.meta/に空ファイル作成（ファイル名を識別子として）
MakeWorkMetaFile () {
    # 末尾に.shがあれば (ユーザ処理は.shを仲介するようにするので.shだけで十分）
    if [[ $1 =~ .sh ]] ; then
        . "$HOME/root/script/sh/_userlib/path.sh"
        . "$HOME/root/script/sh/_lib/path.sh"
        local filename=`basename $1`
        local without_ext=${filename%.*}
        local id=$without_ext
        local metafilepath=$(Join $(GetWorkMetaDir) '.'$id)
        if [ ! -f $metafilepath ]; then
            mkdir -p `GetWorkMetaDir`
            touch $metafilepath
            # 初回のみファイルパスを返す
            echo $metafilepath
        fi
        # 初回以降はパスを返さない
    # エラー
    else
        exit 1
    fi
}
