#!/usr/bin/env bash


vpn_connect() {
    kitty wg-quick up wg0 && ifconfig | grep "wg0: flags=209<UP,POINTOPOINT,RUNNING,NOARP>" && myip=$(curl ifconfig.co/) && country=$(curl ifconfig.co/country) && city=$(curl ifconfig.co/city) && notify-send -i ~/.icons/forest-icons/48x48/status/changes-prevent.svg '✅ Wireguard VPN Connected' \ "🔥 Ip Changed to ${myip} \n ✰ ${country} - ${city}" || notify-send -i ~/.icons/forest-icons/48x48/status/dialog-error.svg "🔥 Wireguard VPN Not Connected" "⚠️ Please Either Manually Check by typing [ sudo wg ] or check your ip"
}

vpn_disconnect() {
    kitty wg-quick down wg0; myip=$(curl ifconfig.co/) && country=$(curl ifconfig.co/country) && city=$(curl ifconfig.co/city) && notify-send -i ~/.icons/forest-icons/48x48/status/changes-allow.svg "🔥 Wireguard VPN Disconnected" \ "🗲 Your current Ip - ${myip} \n ✰ ${country} - ${city}"
}



green=#02fc34
red=#fc0202


vpn_status() {
    if ifconfig | /bin/grep -d skip "wg0" >> /dev/null ; then
      echo %{u"$green"}%{T4}%{F"$green"}Wireguard Connected 
    elif ifconfig | /bin/grep -d skip "tun0" >> /dev/null ; then
      echo %{u"$green"}%{T4}%{F"$green"}Openvpn Connected 
    elif ifconfig | /bin/grep -d skip "utun420" >> /dev/null ; then
      echo %{u"$green"}%{T4}%{F"$green"}Windscribe Connected
    else
      echo Not Connected
    fi
}


# green=#02fc34
# red=#fc0202


# vpn_status() {
#     if ifconfig | /bin/grep -d skip "wg0" >> /dev/null ; then
#       echo %{u"$green"}%{T4}%{F"$green"}Wireguard Connected 
#     elif ifconfig | /bin/grep -d skip "tun0" >> /dev/null ; then
#       echo %{u"$green"}%{T4}%{F"$green"}Openvpn Connected 
#     elif ifconfig | /bin/grep -d skip "utun420" >> /dev/null ; then
#       echo %{u"$green"}%{T4}%{F"$green"}Windscribe Connected
#     else
#       echo %{u"$red"}%{T4}%{F"$red"}Not Connected
#     fi
# }



if  [[ $1 = "--connect" ]]; then
    vpn_connect
elif  [[ $1 = "--disconnect" ]]; then
    vpn_disconnect
elif  [[ $1 = "--status" ]]; then
    vpn_status
fi