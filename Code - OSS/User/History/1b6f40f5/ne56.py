import requests
from urllib.request import urlopen


def download_image(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.urlretrieve(url, full_path)

url = input('Please enter image URL (string):')
file_name = input('Save image as (string):')

download_image(url, 'images/', file_name)