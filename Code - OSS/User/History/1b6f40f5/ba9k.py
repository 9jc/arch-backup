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



search_query = "wow"
# Directory
directory = f"Downloaded/{search_query}{file_name}"
  
# Parent Directory path
parent_dir = "/home/i0xfce/MEGAsync/Projects/Python/Wallpaper_Downloader/"
  
# Path
path = os.path.join(parent_dir, directory)
  
# Create the directory
# 'Nikhil'
try:
    os.makedirs(path, exist_ok = True)
    print("Directory '%s' created successfully" % directory)
except OSError as error:
    print("Directory '%s' can not be created" % directory)
    
    

urllib.request.urlretrieve(urls, directory)