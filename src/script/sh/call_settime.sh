#!/bin/bash

# framework版
. ~/root/script/sh/_userlib/path.sh
. ~/root/script/sh/_lib/path.sh
onetime=$(Join $(GetShellScriptDir) /_framework/onetime.sh)
settime=$(Join $(GetShellScriptDir) ./settime.sh)
$onetime $settime
unset onetime
unset settime

# lib版
#settime=$HOME/root/script/sh/settime.sh
#. $HOME/root/script/sh/_userlib/path.sh
#metafile=$(MakeWorkMetaFile "$settime")
#[ 0 -lt ${#metafile} ] && $settime
#unset metafile
#unset settime

