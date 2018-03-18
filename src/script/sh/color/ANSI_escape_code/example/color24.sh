# https://en.wikipedia.org/wiki/ANSI_escape_code
. ../ansi.sh
. ../SGR_P.sh
function Program () {
    for r in $(seq 0 255) ; do
        for g in $(seq 0 255) ; do
            for b in $(seq 0 255) ; do
                local ansi=`SGR $(Color24 $r $g $b)`
                echo -n -e "$ansi$r:$g:$b "
            done
        done
    done
    echo 
    for r in $(seq 0 255) ; do
        for g in $(seq 0 255) ; do
            for b in $(seq 0 255) ; do
                local ansi=`SGR $(BackgroundColor24 $r $g $b)`
                echo -n -e "$ansi$r:$g:$b "
            done
        done
    done
    echo 
}
Program
