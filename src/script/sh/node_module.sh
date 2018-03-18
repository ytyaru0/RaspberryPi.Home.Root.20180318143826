module=markdonwnit
work=/tmp/work/env/node/
[ ! -d $work ] && mkdir -p $work
if [ ! -d $work$module ]; then
    cp -r ~/root/env/node/$module $work
    export PATH=$PATH:$work$module/node_modules/.bin
fi
unset module
unset work
