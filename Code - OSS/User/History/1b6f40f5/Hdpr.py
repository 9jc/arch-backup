import requests
import urllib.request


url = input('Please enter image URL (string):')
file_name = input('Save image as (string):')


Using urllib, you can get this done instantly.


opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

urllib.request.urlretrieve(URL, "images/0.jpg")