. ../ansi.sh
echo "----- ansi.sh -----"
echo `SGR`
echo `SGR_RESET`

. ../color_define.sh
echo "----- color_define.sh -----"
echo `SGR ${COLORS["R"]}`
echo `SGR ${COLORS["G"]}`
echo `SGR ${COLORS["B"]}`
echo -e "`SGR ${COLORS["R"]}` RRRRRRRRRR"
echo -e "`SGR ${COLORS["G"]}` GGGGGGGGGG"
echo -e "`SGR ${COLORS["B"]}` BBBBBBBBBB"
R=`SGR ${COLORS["R"]}`
G=`SGR ${COLORS["G"]}`
B=`SGR ${COLORS["B"]}`
echo -e "$R RRRRRRRRRR"
echo -e "$G GGGGGGGGGG"
echo -e "$B BBBBBBBBBB"
echo -e -n `SGR_RESET`

. ../SGR_P.sh
echo "----- SGR_P.sh -----"
echo `SGR $(SGR_P ${SGR_P["Bold"]} ${COLORS["R"]})`
echo `SGR $(SGR_P ${SGR_P["Underline"]} ${COLORS["G"]})`
echo `SGR $(SGR_P ${SGR_P["Reverse"]} ${COLORS["B"]})`
echo `SGR $(SGR_P $(Color24 255 196 0))`
echo `SGR $(SGR_P $(BackgroundColor24 255 0 255))`
BR=`SGR $(SGR_P ${SGR_P["Bold"]} ${COLORS["R"]})`
UG=`SGR $(SGR_P ${SGR_P["Underline"]} ${COLORS["G"]})`
RB=`SGR $(SGR_P ${SGR_P["Reverse"]} ${COLORS["B"]})`
COL24=`SGR $(SGR_P $(Color24 255 196 0))`
BGCOL24=`SGR $(SGR_P $(BackgroundColor24 255 0 255))`
echo -e "$BR RRRRRRRRRR"
echo -e "$UG GGGGGGGGGG"
echo -e "$RB BBBBBBBBBB"
echo -e "$COL24 SOME_COLOR_24bit"
echo -e "$BGCOL24 SOME_BACKGROUND_COLOR_24bit"
echo -e -n `SGR_RESET`

. ../color8_define.sh
echo "----- color8_define.sh -----"
echo `SGR $(SGR_P $(Color8 ${COLORS["R"]}))`
echo `SGR $(SGR_P $(Color8 ${COLORS["G"]}))`
echo `SGR $(SGR_P $(Color8 ${COLORS["B"]}))`
echo `SGR $(SGR_P $(Color8 $(GetColor 5 3 1)))` # 0..5 (6bit color)
echo `SGR $(SGR_P $(BackgroundColor8 $(GetColor 5 3 1)))`
R=`SGR $(SGR_P $(Color8 ${COLORS["R"]}))`
G=`SGR $(SGR_P $(Color8 ${COLORS["G"]}))`
B=`SGR $(SGR_P $(Color8 ${COLORS["B"]}))`
COL8=`SGR $(SGR_P $(Color8 $(GetColor 5 3 1)))`
BGCOL8=`SGR $(SGR_P $(BackgroundColor8 $(GetColor 5 3 1)))`
echo -e "$R RRRRRRRRRR"
echo -e "$G GGGGGGGGGG"
echo -e "$B BBBBBBBBBB"
echo -e "$COL8 SOME_COLOR_8bit(216)"
echo -e "$BGCOL8 SOME_BACKGROUND_COLOR_8bit(216)"
echo -e -n `SGR_RESET`

