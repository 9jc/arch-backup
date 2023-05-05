#!/usr/bin/env bash

# Color files
PFILE="$HOME/.config/polybar/forest/colors.ini"
RFILE="$HOME/.config/polybar/forest/scripts/rofi/colors.rasi"

# Change colors
change_color() {
	# polybar
	sed -i -e "s/background = #.*/background = $BG/g" $PFILE
	sed -i -e "s/foreground = #.*/foreground = $FG/g" $PFILE
	sed -i -e "s/themes = #.*/themes = $AC/g" $PFILE
	sed -i -e "s/text = #.*/text = $BG/g" $PFILE
	
	# rofi
	cat > $RFILE <<- EOF
	/* colors */

	* {
	  al:   #00000000;
	  bg:   ${BG}FF;
	  bga:  ${BGA}FF;
	  fg:   ${FG}FF;
	  ac:   ${AC}FF;
	  se:   ${SE}FF;
	}
	EOF
	
	polybar-msg cmd restart
}

if  [[ $1 = "--dark-pink" ]]; then
	BG="#180A0A"
	FG="#FFDDEE"
	BGA="#323232"
	SEP="#524A4E"
	AC="#F10086"
	SE="#F10086"
	change_color
elif  [[ $1 = "--dark-blue" ]]; then
	BG="#001524"
	FG="#caf0f8"
	BGA="#263035"
	SEP="#3F5360"
	AC="#0aefff"
	SE="#0aefff"
	change_color
elif  [[ $1 = "--dark-green" ]]; then
	BG="#191A19"
	FG="#D8E9A8"
	BGA="#1E5128"
	SEP="#4E9F3D"
	AC="#49FF00"
	SE="#49FF00"
	change_color
elif  [[ $1 = "--dark-yellow" ]]; then
	BG="#000000"
	FG="#EEEEEE"
	BGA="#810034"
	SEP="#FF005C"
	AC="#FFF600"
	SE="#FFF600"
	change_color
elif  [[ $1 = "--grey-green" ]]; then
	BG="#26001B"
	FG="#EEEEEE"
	BGA="#263035"
	SEP="#393E46"
	AC="#4ECCA3"
	SE="#4ECCA3"
	change_color
elif  [[ $1 = "--grey-green" ]]; then
	BG="#232931"
	FG="#EEEEEE"
	BGA="#263035"
	SEP="#393E46"
	AC="#4ECCA3"
	SE="#4ECCA3"
	change_color
elif  [[ $1 = "--grey-green" ]]; then
	BG="#232931"
	FG="#EEEEEE"
	BGA="#263035"
	SEP="#393E46"
	AC="#4ECCA3"
	SE="#4ECCA3"
	change_color
elif  [[ $1 = "--grey-green" ]]; then
	BG="#232931"
	FG="#EEEEEE"
	BGA="#263035"
	SEP="#393E46"
	AC="#4ECCA3"
	SE="#4ECCA3"
	change_color
elif  [[ $1 = "--dark-red" ]]; then
	BG="#000000"
	FG="#E5E9F0"
	BGA="#5a0001"
	SEP="#8b0000"
	AC="#FF0000"
	SE="#d30004"
	change_color
elif  [[ $1 = "--gruvbox" ]]; then
	BG="#282828"
	FG="#EBDBB2"
	BGA="#313131"
	SEP="#505050"
	AC="#FB4934"
	SE="#8EC07C"
	change_color
elif  [[ $1 = "--dark" ]]; then
	BG="#141C21"
	FG="#93A1A1"
	BGA="#1E262B"
	SEP="#3C4449"
	AC="#D12F2C"
	SE="#33C5BA"
	change_color
elif  [[ $1 = "--cherry" ]]; then
	BG="#1F1626"
	FG="#FFFFFF"
	BGA="#292030"
	SEP="#473F4E"
	AC="#D94084"
	SE="#4F5D95"
	change_color
else
	cat <<- _EOF_
	No option specified, Available options:
	--dark-pink  --dark-blue    --nord    --gruvbox    --dark    --cherry
	_EOF_
fi
