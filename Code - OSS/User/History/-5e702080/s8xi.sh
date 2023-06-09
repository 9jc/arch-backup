#!/usr/bin/env bash

# Color files Polybar
Polybar="$HOME/.config/polybar/colors.ini"
Rolfi-1="$HOME/.config/polybar/scripts/rofi/colors.rasi"
Rolfi-2="$HOME/.config/rofi/launchers/colorful/colors.rasi"
Rolfi-3="$HOME/.config/rofi/powermenu/colors.rasi"
# Color files Overall
Xcolor="$HOME/.Xresources.d/.Xcolors"
Kitty="$HOME/.config/kitty/current-theme.conf"
Conky="$HOME/.config/conky/rings-v1.2.1.lua"
Cava="$HOME/.config/cava/config"
Glava="$HOME/.config/glava/bars.glsl"
Bashtop="$HOME/.config/bashtop/themes/embark.theme"
Discord="$HOME/.config/BetterDiscord/themes/ClearVision_v6.theme.css"
Dmenu="$HOME/.config/sxhkd/scripts/dmenu.sh"

# Gets random wallpaper
my_array=(/$HOME/Pictures/Wallpapers/*)

# Get colors
pywal_get() {
    wal -t -e -i ${my_array[$(( $RANDOM % ${#my_array[@]}))]} -a 80
}

# Change colors
change_theme_polybar() {

	# polybar
	sed -i -e "s/background = #.*/background = ${BG}/g" $Polybar
        sed -i "/background-alt = #8C/c background-alt = #8C${BGA}" $Polybar
        sed -i -e "s/foreground = #.*/foreground = ${FG}/g" $Polybar
	sed -i -e "s/themes = #.*/themes = $SH14/g" $Polybar
	
	# rofi
	cat > $Rolfi-1 <<- EOF
	/* colors */

	* {
	  al:    ${FG}FF;
	  bg:    ${BG}FF;
	  bga:   ${BG}FF;
	  fg:   ${SH15}FF;
	  ac:   ${SH14}FF;
	  se:    ${SH14}FF;
	}
	EOF
	polybar-msg cmd restart
  }


change_theme_overall() {

      # Changes conky color
      sed -i "/current1 = 0x/c current1 = 0x${CONKY}" $Conky

      # Dmenu
      sed -i -e "s/BG=#.*/BG=${BG}/g" $Dmenu
      sed -i -e "s/FG=#.*/FG=${SH14}/g" $Dmenu

      # Changes cava gradient
      sed -i "/gradient_color_1 = '/c gradient_color_1 = '${SH14}'" $Cava
      sed -i "/gradient_color_2 = '/c gradient_color_2 = '${SH13}'" $Cava
      sed -i "/gradient_color_3 = '/c gradient_color_3 = '${SH12}'" $Cava
      sed -i "/gradient_color_4 = '/c gradient_color_4 = '${SH11}'" $Cava
      sed -i "/gradient_color_5 = '/c gradient_color_5 = '${SH4}'" $Cava
      sed -i "/gradient_color_6 = '/c gradient_color_6 = '${SH3}'" $Cava
      sed -i "/gradient_color_7 = '/c gradient_color_7 = '${SH2}'" $Cava
      sed -i "/gradient_color_8 = '/c gradient_color_8 = '${SH1}'" $Cava
      # reloads cava without needed to close it
      pkill -USR1 cava
  
      # Changes Glava theme
      sed -i "/#define COLOR (#/c #define COLOR (${SH14} * GRADIENT)" $Glava
  
      # Changes Discord theme
      sed -i "/--main-color: /c\  --main-color: ${SH14};" $Discord
      sed -i "/--hover-color:/c\  --hover-color: ${SH1};" $Discord


      # Changes Kitty theme
      cat > $Kitty <<- EOFE
background            ${BG}
foreground            ${FG}
cursorColor           ${SH14}
selection_background  ${SH1}
color0                ${SH0}
color1                ${SH1}
color2                ${SH2}
color3                ${SH3}
color4                ${SH14}
color5                ${SH5}
color6                ${FG}
color7                ${FG}
color8                ${SH8}
color9                ${SH9}
color10               ${SH10}
color11               ${SH12}
color12               ${SH12}
color13               ${SH13}
color14               ${FG}
color15               ${FG}
selection_foreground  ${SH0}
EOFE

      # Changes St theme
      cat > $Xcolor <<- EOF
! Colors
*.background: ${BG}
*.foreground: ${FG}
*.cursorColor: ${SH14}
*.selection_background: ${SH1}
*.color0: ${SH0}
*.color1: ${SH1}
*.color2: ${SH2}
*.color3: ${SH3}
*.color4: ${SH14}
*.color5: ${SH5}
*.color6: ${FG}
*.color7: ${FG}
*.color8: ${SH8}
*.color9: ${SH9}
*.color10: ${SH10}
*.color11: ${SH12}
*.color12: ${SH12}
*.color13: ${SH13}
*.color14: ${FG}
*.color15: ${FG}
*.selection_foreground: ${SH0}
	EOF
        # rofi
	      cat > $Rolfi-3 <<- EOF
	/* colors */

	* {
	  al:    ${FG}FF;
	  bg:    ${BG}FF;
	  bga:   ${BG}FF;
	  fg:   ${SH15}FF;
	  ac:   ${SH14}FF;
	  se:    ${SH14}FF;
	}
	EOF
        

        # Changes Bspwm Border Color
        bspc config normal_border_color    "${SH1}"
        bspc config active_border_color     "${SH13}"
        bspc config focused_border_color    "${SH14}"
        bspc config presel_feedback_color   "${SH2}"

	xrdb merge ~/.Xresources &
}


# Extracting Colors From Pywall
if [[ $1 = "--theme" ]]; then

    # Generating colors accoring to the wallpaper
    pywal_get "$1"

    # Source the pywal color file
    . "$HOME/.cache/wal/colors.sh"
    BG=`printf "%s\n" "$background"`
    BGA=`printf $background | cut -c2-`
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

    # Conky Color
    CONKY=`printf $color14 | cut -c2-`
    
    change_theme_polybar
    change_theme_overall
    printf "\n Successfully changed the theme!! \n"
else
    echo "./pywal.sh --theme"echo -e "\n Usage : ./pywal.sh --theme \n"

fi
