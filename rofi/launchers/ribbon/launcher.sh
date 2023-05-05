#!/usr/bin/env bash

## Author  : Aditya Shakya
## Mail    : adi1090x@gmail.com
## Github  : @adi1090x
## Twitter : @adi1090x

# Available Styles
# >> Created and tested on : rofi 1.6.0-1
#
# ribbon_top		ribbon_top_round		ribbon_bottom	 	ribbon_bottom_round
# ribbon_left		ribbon_left_round		ribbon_right		ribbon_right_round
# full_bottom		full_top				full_left			full_right

theme="full_right"

dir="$HOME/.config/rofi/launchers/ribbon"
styles=($(ls -p --hide="colors.rasi" $dir/styles))
# color="${styles[$(( $RANDOM % 8 ))]}"


. "$HOME/.cache/wal/colors.sh"

TH=`printf "%s\n" "$color14"`
BG=`printf "%s\n" "$background"`
FG=`printf "%s\n" "$foreground"`
FW=`printf "%s\n" "$color11"`
BRQ=`printf "%s\n" "$color8"`
BR=`printf "%s\n" "$color9"`
FA=`printf "%s\n" "$color7"`


# overwrite colors file

cat > $dir/colors.rasi <<- EOF
* {
    background:                     $BG;
    background-alt:                 $FA;
    foreground:                     $FA; 
    border:               			$BR;
    border-alt:               		$FW;
    selected:               		$BRQ;
    urgent:                         $TH;
}

EOF


# comment this line to disable random colors
# sed -i -e "s/@import .*/@import \"$color\"/g" $dir/styles/colors.rasi         

# comment these lines to disable random style
#themes=($(ls -p --hide="launcher.sh" --hide="styles" $dir))
#theme="${themes[$(( $RANDOM % 12 ))]}"

rofi -no-lazy-grab -show drun -modi drun -theme $dir/"$theme"
