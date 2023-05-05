#!/usr/bin/env bash

vpn_connect() {
    kitty wg-quick up wg0; sudo wg | grep '[\]' && myip=$(curl ifconfig.co/) && country=$(curl ifconfig.co/country) && city=$(curl ifconfig.co/city) && notify-send -i ~/.icons/forest-icons/48x48/status/changes-prevent.svg "✅ Wireguard VPN Connected" \ "🔥 Ip Changed to ${myip} \n ✰ ${country} - ${city}" || notify-send -i ~/.icons/forest-icons/48x48/status/changes-allow.svg "🔥 Wireguard VPN Not Connected"
}

vpn_disconnect() {
    kitty wg-quick down wg0; myip=$(curl ifconfig.co/) && country=$(curl ifconfig.co/country) && city=$(curl ifconfig.co/city) && notify-send -i ~/.icons/forest-icons/48x48/status/changes-allow.svg "🔥 Wireguard VPN Disconnected" \ "🗲 Your current Ip - ${myip} \n ✰ ${country} - ${city}"
}
1



if  [[ $1 = "--connect" ]]; then
    vpn_connect
elif  [[ $1 = "--disconnect" ]]; then
    vpn_disconnect
fi