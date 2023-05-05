import requests
import urllib.request
import re
import os

os.system("clear")
# Gets the Urls File name
def get_url_file_name(url):
    url = url.split("#")[0]
    url = url.split("?")[0]
    return os.path.basename(url)

# image_link_nsfw = input('Please enter image URL (string):')
# search_query = "hot"

def download_img(url_image, search_query, apply_wall):
    # Asking user to input url
    file_name = (get_url_file_name(url_image))
    
      
    print(search_query)
    print(url_image)
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
        
        # print("Directory '%s' created successfully" % directory)
    except OSError as error:
        print("Directory '%s' can not be created" % directory)
    

    urllib.request.urlretrieve(url_image, os.path.join(path, os.path.basename(file_name)))
    #
    # def user_ask():
    #     input1 = input("Do you want to apply this wallpaper (yes/no/preview):")
    #     return input1
    #
    # user_ask2 = user_ask()

# Apply the wallpaper 
    def apply_wallpaper(k):
        if k == "yes" or k == "y":
            os.system(f"feh --bg-fill {path}/{file_name}")
        elif k == "preview" or k == "p":
            os.system(f"feh -z  {path}/{file_name}")
        elif k == "no" or k == "n":
            print("Done!!")
            user_ask()
        else:
            print("unknown option try again")
    apply_wallpaper(k=apply_wall)
#download_img(url_image=image_link_nsfw, search_query=search_query)
