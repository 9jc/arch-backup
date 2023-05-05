#! /usr/bin/python
import sys
import subprocess
import json
import os
import time
from pathlib import Path

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from piratebay import *
from spinner import Spinner , add_cursor
from message import *


def write_table(movie_list):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", width=12)
    table.add_column("Title")
    table.add_column("Size", justify="right")
    table.add_column("Seeders", justify="right")
    table.add_column("Leeches", justify="right")

    for i , obj in enumerate( movie_list ):
        table.add_row(str(i+1) , obj["title"] , str(obj["size"]),str(obj["seeders"]) , str(obj["leeches"]))

    console.print(table)
    return

def greet_bye():
    print("\nsee ya 👋")


def parse_config():
    app_dir = "/".join(os.path.realpath(__file__).split("/")[:-2])
    config_path = os.path.join(app_dir , "config.json")

    default_value = ("webtorrent" , "mpv")
    players = ["mpv" , "vlc"]
    clients = ["webtorrent" , "peerflix"]

    if not Path(config_path).is_file():
        return default_value

    with open(config_path) as f:
        config = json.loads(f.read())
    
    if config["config"]["player"] and config["config"]["client"]:
        if config["config"]["player"] in players and config["config"]["client"] in clients:
            return (  config["config"]["client"] , config["config"]["player"] )
    
    return default_value
        
def stream(mag_url):
    client , player = parse_config()
    subprocess.run([client , mag_url , f"--{player}" ])


console = Console()

try:
    os.system("clear||cls")
    start_message = input(intro)

    # Option 1 - Stream Torrent------------------------- 1
    if start_message == "1":
        os.system("clear||cls")

        stream_what = input(choose_option)

        # Prompt Search for torrent
        if stream_what == "1":
            os.system("clear||cls")
            print(f"{you_choose} {stream_what}")
            query = Prompt.ask(search_stream_torrent)
        # Prompt to give magnet url
        elif stream_what == "2":
            os.system("clear||cls")
            print(f"{you_choose} {stream_what}")
            mag_url = Prompt.ask(link_stream_torrent)
            stream(mag_url)
        # Else Exit
        else:
            time.sleep(2)
            os.system("clear||cls")
            exit(1)
    # Option 2 - Download Torrent--------------------- 2
    elif start_message == "2":
        print("Not Ready")
        time.sleep(2)
        os.system("clear||cls")
        exit(1)

    # Exit-------------------------------------------- 3
    else:
        greet_bye()
        os.system("clear||cls")
        exit(1)

    # Finding Torrents ------------------------------- 4
    print("  Finding torrents" , end="\r")

    with Spinner():
        movie_list = pirate(query=query)["movie_info"]

    if len(movie_list) == 0:
        greet_bye()
        exit(1)

    # Write Tables ----------------------------------- 5
    write_table(movie_list)

    # Select Movie ----------------------------------- 6
    movie_ind = Prompt.ask("Select your fav" , default="1")
    if int(movie_ind) >= len(movie_list):
        mag_url = movie_list[-1]["magnet_url"]
        print(mag_url)
        time.sleep(20)
    else:
        mag_url = movie_list[int(movie_ind)-1]["magnet_url"]
        print(mag_url)
        time.sleep(20)

except KeyboardInterrupt:
    add_cursor()
    greet_bye()
    exit(1)

print("Enjoy! Less seeds may take more time\nStreaming will start after 1% of downloading")
stream(mag_url)





