#!/usr/bin/env bash

SDIR="$HOME/.config/polybar/forest/scripts"

# Launch Rofi
MENU="$(rofi -no-config -no-lazy-grab -sep "|" -dmenu -i -p '' \
-theme $SDIR/rofi/styles.rasi \
<<< "  Dark-Pink|  Dark-Blue|  Nord|  Gruvbox|  Dark|  Cherry|")"
            case "$MENU" in
				*Dark-Pink) "$SDIR"/styles.sh --dark-pink ;;
				*Dark-Blue) "$SDIR"/styles.sh --dark-blue ;;
				*Nord) "$SDIR"/styles.sh --nord ;;
				*Gruvbox) "$SDIR"/styles.sh --gruvbox ;;
				*Dark) "$SDIR"/styles.sh --dark ;;
				*Cherry) "$SDIR"/styles.sh --cherry ;;
            esac
