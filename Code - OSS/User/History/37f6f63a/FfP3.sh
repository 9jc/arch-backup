#!/usr/bin/env bash

# Color files
XFILE="$HOME/.Xresources"


# Change colors
change_color() {
	# polybar
	
	# rofi
	cat > $XFILE <<- EOF
Xft.antialias:	1
Xft.hinting:	1
Xft.autohint:	0
Xft.hintstyle:	hintslight
Xft.rgba:	rgb
Xft.lcdfilter:	lcddefault

! window padding
st.borderpx: 18

!-- values between 0.1  - 1.0 --! 

st.alpha: .8
st.font:           JetBrainsMono Nerd Font:style:medium:pixelsize=20

! Colors
*.background: ${BG}
*.foreground: ${FG}
*.cursorColor: ${SH14}
*.selection_background: ${SH1}
*.color0: ${SH0}
*.color1: ${SH1}
*.color2: ${SH2}
*.color3: ${SH3}
*.color4: ${SH4}
*.color5: ${SH5}
*.color6: ${SH6}
*.color7: ${SH7}
*.color8: ${SH8}
*.color9: ${SH9}
*.color10: ${SH10}
*.color11: ${SH11}
*.color12: ${SH12}
*.color13: ${SH13}
*.color14: ${FG}
*.color15: ${FG}
*.selection_foreground: ${SH0}

! Urxvt Settings
URxvt.scrollBar: false
URxvt.scrollBar_right: false
URxvt*depth: 32
URxvt.background: ${BG}
URxvt*internalBorder: 50
urxvt.iso14755: false
urxvt.keysym.Shift-Control-V: eval:paste_clipboard
urxvt.keysym.Shift-Control-C: eval:selection_to_clipboard
URxvt.perl-ext-common: default,matcher
URxvt.url-launcher: /usr/bin/xdg-open
URxvt.matcher.button: 1

Xcursor.theme: Volantes_Light_Curser

! just remove this if you dont use my tabbed

tabbed.selfgcolor:   ${FG}
tabbed.selbgcolor:   ${SH0}

tabbed.normfgcolor:  ${SH11}
tabbed.normbgcolor:  ${SH7}
	EOF

	xrdb merge ~/.Xresources &
	# bspc wm -r &
}

# Main

if [[ "$1" ]]; then
	# Source the pywal color file
	. "$HOME/.cache/wal/colors.sh"
	BG=`printf "%s\n" "$background"`
	FG=`printf "%s\n" "$foreground"`
	FGA=`printf "%s\n" "$color7"`
	SH0=`printf "%s\n" "$color0"`
	SH1=`printf "%s\n" "$color1"`
	SH2=`printf "%s\n" "$color2"`
	SH3=`printf "%s\n" "$color3"`
	SH4=`printf "%s\n" "$color4"`
	SH5=`printf "%s\n" "$color5"`
	SH6=`printf "%s\n" "$color6"`
	SH7=`printf "%s\n" "$color7"`
	SH8=`printf "%s\n" "$color8"`
	SH9=`printf "%s\n" "$color9"`
	SH10=`printf "%s\n" "$color10"`
	SH11=`printf "%s\n" "$color11"`
	SH12=`printf "%s\n" "$color12"`
	SH13=`printf "%s\n" "$color13"`
	SH14=`printf "%s\n" "$color14"`
	SH15=`printf "%s\n" "$color15"`
	# SH9 = $(printf $color14 | cut -c2-)
	change_color
else
	echo "[!] 'pywal' is not installed."
fi
