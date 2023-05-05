#!/usr/bin/env bash

DIR="$HOME/.config/polybar/cuts"

# Terminate already running bar instances

killall -q polybar
bspc config top_padding 30
bspc config bottom_padding 30

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch the preview bar
polybar -q top -c "$DIR"/preview.ini &
polybar -q mid -c "$DIR"/preview.ini &
polybar -q bottom -c "$DIR"/preview.ini &
