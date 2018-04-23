. $HOME/root/script/sh/_lib/path.sh
node_env_root=$HOME/root/env/node
for dname in `GetChildrenDirnames $node_env_root`; do
    export PATH=$PATH:$node_env_root/$dname/node_modules/.bin
done
unset node_env_root
#module=markdonwnit
#work=/tmp/work/env/node/
#[ ! -d $work ] && mkdir -p $work
#if [ ! -d $work$module ]; then
#    cp -r ~/root/env/node/$module $work
#    export PATH=$PATH:$work$module/node_modules/.bin
#fi
#unset module
#unset work
