import os
import time
from colorama import Fore, init, Style, Back
import datetime

# Getting Date, time and macro second
date_now = datetime.datetime.now()

date1 = (date_now.strftime("%x"))
time1 = (date_now.strftime("%X"))
micro_sec = (date_now.strftime("%f"))


red = Fore.RED
magenta = Fore.MAGENTA
yellow = Fore.YELLOW
blue = Fore.BLUE
green = Fore.GREEN
white = Fore.WHITE
red = Fore.LIGHTRED_EX
lblue = Fore.LIGHTBLUE_EX
cyan = Fore.LIGHTCYAN_EX
lgreen = Fore.LIGHTGREEN_EX
lmagenta = Fore.LIGHTMAGENTA_EX
lwhite = Fore.LIGHTWHITE_EX
lblack = Fore.LIGHTBLACK_EX
lyellow = Fore.LIGHTYELLOW_EX

#Modules
intro = (f"""

{cyan}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{red} Torrent Downloader/Streamer
{cyan}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{yellow} Modules Avalible
{green}
1 ━  Stream Torrent
2 ━  Download Torrent
3 -  Exit Program
{cyan}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{red}
➤ """)

# Streaming Torrent
search_stream_torrent = (f"\n{yellow} {magenta} Enter the search term you want to [ Stream Torrent ] of {red}➤ ")
link_stream_torrent = (f"\n{yellow} {magenta} Enter the magnet link you want to [ Stream Torrent ] from {red}➤ ")

# Download Torrent
search_download_torrent = (f"\n{yellow} {magenta} Enter the search term you want to [ Download Torrent ] of {red}➤ ")
link_download_torrent = (f"\n{yellow} {magenta} Enter the magnet link you want to [ Download Torrent ] from {red}➤ ")


help_me = (f"""
{cyan}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{yellow} List of avalible tags and search terms!!{cyan}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{yellow}
Query Type | Tags | Examples    {cyan}|
--------------------------------|{green}
 People   | 100  | Minimalstic |
 Sfw      | 010  | Anime       | 
 Nsfw     | 001  | Po*n        |
 Mixed    | 111  | Black       |{cyan}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{yellow}Press {red}"q" to quit {yellow} / any command to start again {red}➤ """)
error = f"""

{red} Error 404 - Unknown Command Detected...

"""


