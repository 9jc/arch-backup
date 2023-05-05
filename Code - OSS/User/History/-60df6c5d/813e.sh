#!/usr/bin/env bash

SDIR="$HOME/.config/polybar/forest/scripts"

# Launch Rofi
MENU="$(rofi -no-config -no-lazy-grab -sep "|" -dmenu -i -p '' \
-theme $SDIR/rofi/styles.rasi \
<<< "  Dark Blue|  Nord|  Gruvbox|  Dark|  Cherry|")"
            case "$MENU" in
				*Darkblue) "$SDIR"/styles.sh --darkblue ;;
				*Nord) "$SDIR"/styles.sh --nord ;;
				*Gruvbox) "$SDIR"/styles.sh --gruvbox ;;
				*Dark) "$SDIR"/styles.sh --dark ;;
				*Cherry) "$SDIR"/styles.sh --cherry ;;
            esac
