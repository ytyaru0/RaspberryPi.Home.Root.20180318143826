path_this_dir=$(cd $(dirname $0); pwd)
path_target=$(dirname "${path_this_dir}")"/src/{{filename}}.sh"
. ${path_target}
res=$({{funcname}})
[[ $res != 'Hello' ]] && echo NG!!
