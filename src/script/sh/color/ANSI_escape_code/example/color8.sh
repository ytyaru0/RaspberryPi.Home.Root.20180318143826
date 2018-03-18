# https://en.wikipedia.org/wiki/ANSI_escape_code
function Program () {
    . ../ansi.sh
    . ../SGR_P.sh
    . ../color8_define.sh
    echo -e -n `SGR_RESET`
    echo "----- Standard colors -----"
    for x in `GetStandardColors` ; do
        local ansi=`SGR $(Color8 $x)`
        local values="$values$ansi$x "
    done
    echo -e "$values`SGR_RESET`"
    unset values
    echo "----- Bright colors -----"
    for x in `GetBrightColors` ; do
        local ansi=`SGR $(Color8 $x)`
        local values="$values$ansi$x "
    done
    echo -e "$values`SGR_RESET`"
    unset values
    echo "----- Gray scale -----"
    for x in `GetGrayScale` ; do
        local ansi=`SGR $(Color8 $x)`
        local values="$values$ansi$x "
    done
    echo -e "$values`SGR_RESET`"
    unset values
    echo "----- 216 color -----"
    for R in `seq 0 5` ; do
        for G in `seq 0 5` ; do
            for B in `seq 0 5` ; do
                local ansi=`SGR $(Color8 $(GetColor $R $G $B))`
                local values="$values$ansi$R$G$B "
            done
        done
    done
    echo -e "$values`SGR_RESET`"
    unset values
    echo "----- 256 colors -----"
    for x in $(seq 0 255) ; do
        local ansi=`SGR $(Color8 $x)`
        local values="$values$ansi$x "
    done
    echo -e "$values`SGR_RESET`"
    unset values
    for x in $(seq 0 255) 0 ; do
        local ansi=`SGR $(BackgroundColor8 $x)`
        local values="$values$ansi$x "
    done
    echo -e "$values`SGR_RESET`"
    unset values
}
Program
