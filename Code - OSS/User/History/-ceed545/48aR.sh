#!/usr/bin/env bash

# Add this script to your wm startup file.

DIR="$HOME/.config/polybar/cuts"

# Terminate already running bar instances
killall -q polybar

#Bspwm gaps
bspc config top_padding 30
bspc config bottom_padding 30

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch the bar
polybar -q top -c "$DIR"/config.ini &
polybar -q bottom -c "$DIR"/config.ini &
