#!/usr/bin/env bash

SDIR="$HOME/.config/polybar/forest/scripts"

# Launch Rofi
MENU="$(rofi -no-config -no-lazy-grab -sep "|" -dmenu -i -p '' \
-theme $SDIR/rofi/styles.rasi \
<<< " Dark-Pink |  Dark-Pink2 |  Dark-Purple |  Dark-Blue |  Dark-Cyan |  Dark-Green |  Dark-Lgreen |  Dark-Red |  Dark-Yellow |  Dark-Orange |  Dark-White |  Dark-Brown |  Grey-Blue |  Grey-Green |  Gruvbox |  Dark |  Cherry")"
            case "$MENU" in
				*Dark-Pink) "$SDIR"/styles.sh --dark-pink ;;
				*Dark-Pink2) "$SDIR"/styles.sh --dark-pink2 ;;
				*Dark-Purple) "$SDIR"/styles.sh --dark-purple ;;
				*Dark-Blue) "$SDIR"/styles.sh --dark-blue ;;
				*Dark-Cyan) "$SDIR"/styles.sh --dark-cyan ;;
				*Dark-Green) "$SDIR"/styles.sh --dark-green ;;
				*Dark-Lgreen) "$SDIR"/styles.sh --dark-lgreen ;;
				*Dark-Red) "$SDIR"/styles.sh --dark-red ;;
				*Dark-Yellow) "$SDIR"/styles.sh --dark-yellow ;;
				*Dark-Orange) "$SDIR"/styles.sh --dark-orange ;;
				*Dark-White) "$SDIR"/styles.sh --dark-white ;;
				*Dark-Brown) "$SDIR"/styles.sh --dark-brown ;;
				*Grey-Blue) "$SDIR"/styles.sh --grey-blue ;;
				*Grey-Green) "$SDIR"/styles.sh --grey-green ;;
				*Gruvbox) "$SDIR"/styles.sh --gruvbox ;;
				*Dark) "$SDIR"/styles.sh --dark ;;
				*Cherry) "$SDIR"/styles.sh --cherry ;;
            esac
