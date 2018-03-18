# https://en.wikipedia.org/wiki/ANSI_escape_code
function Program () {
    . ../ansi.sh
    . ../SGR_P.sh
    . ../color_define.sh

    echo "----- 連想配列指定 -----"
    for key in ${!COLORS[@]};
    do
        local ansi=`SGR ${COLORS[$key]}`
        local values="$values$ansi${COLORS[$key]} "
    done
    echo -e "$values`SGR_RESET`"
    unset values

    for key in ${!COLORS[@]};
    do
        local ansi=`SGR $(SGR_P ${SGR_P['Bold']} ${COLORS[$key]})`
        local values="$values$ansi${COLORS[$key]} "
    done
    echo -e "$values`SGR_RESET`"
    unset values

    for key in ${!BG_COLORS[@]};
    do
        local ansi=`SGR ${BG_COLORS[$key]}`
        local values="$values$ansi${BG_COLORS[$key]} "
    done
    echo -e "$values`SGR_RESET`"
    unset values

    echo "----- マジックナンバー指定 -----"
    for x in $(seq 30 37) $(seq 90 97) ; do
        local ansi=`SGR $x`
        local values="$values$ansi$x "
    done
    echo -e "$values`SGR_RESET`"
    unset values

    for x in $(seq 30 37) $(seq 90 97) ; do
        local ansi=`SGR $(SGR_P 01 $x)`
        local values="$values$ansi$x "
    done
    echo -e "$values`SGR_RESET`"
    unset values

    for x in  $(seq 40 47) $(seq 100 107) ; do
        local ansi=`SGR $x`
        local values="$values$ansi$x "
    done
    echo -e "$values`SGR_RESET`"
    unset values
}
Program
