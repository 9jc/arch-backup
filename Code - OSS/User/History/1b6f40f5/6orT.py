import requests
import urllib.request
import re
import os

# Gets the Urls File name
def get_url_file_name(url):
    url = url.split("#")[0]
    url = url.split("?")[0]
    return os.path.basename(url)

# Asking user to input url
urls = input('Please enter image URL (string):')
file_name = (get_url_file_name(urls))

# Downloading url
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)


# Directory
directory = f"Downloaded/{search_query}"
  
# Parent Directory path
parent_dir = "/home/i0xfce/MEGAsync/Projects/Python/Wallpaper_Downloader/"
  
# Path
path = os.path.join(parent_dir, directory)
  
# making the folder
try:
    os.makedirs(path, exist_ok = True)
    print("Directory '%s' created successfully" % directory)
except OSError as error:
    print("Directory '%s' can not be created" % directory)
    

urllib.request.urlretrieve(urls, os.path.join(path, os.path.basename(file_name)))
# Apply the wallpaper 
apply_wallpaper = input("Do you want to apply this wallpaper (yes/no/preview):")
if apply_wallpaper == "yes" or "y":
    os.system(f"feh --bg-fill {path}/{file_name}")
elif apply_wallpaper == "no" or "n":
    os.system(f"feh ")
