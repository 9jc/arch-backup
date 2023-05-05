from colorama import Fore, init, Style, Back

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
{red} Simple Text Editor
{cyan}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{yellow} Modules Avalible
{green}
1 ━  Edit Text
2 ━  Print Numbers
3 -  Exit Program
{cyan}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{red}
➤ """)

normWall = (f"""

{cyan}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{red} Edit Text
{cyan}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{green}1 ━  Replace Word with another word
{green}2 ━  Capitilize etc...
{green}3 ━  Add Sufix and Prefix
{green}4 ━  Add Sufix and Prefix to list of words
{red}h ━   Help Me Choose!!
{cyan}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{red}
➤ """)

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
