# $1: 仮想環境名 (auto_github, ranger)
[ $# -lt 1 ] && { echo "引数エラー。仮想環境名をください。: $@"; exit 1; }
. ~/root/env/py/${1}/bin/activate
. ~/root/script/sh/color/PS1.sh ${1}

