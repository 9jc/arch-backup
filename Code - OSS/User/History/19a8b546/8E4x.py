import datetime
import os

# date_now = datetime.datetime.now()

# date1 = (date_now.strftime("%x"))
# time1 = (date_now.strftime("%X"))
# micro_sec = (date_now.strftime("%f"))


# search_query = "ll"


# file_all_links = open(f"{search_query}_daily.txt", ("a"))

# for m in range(10, 600):
#     text = str(m)
#     line_breaker = f"-----------------------------------{micro_sec}[ {search_query} | Date ~ {date1} - {time1} ] \-------------------------------------n"
#     space = ('\n') 
    
#     file_all_links.write(line_breaker)
#     file_all_links.write(text)
#     file_all_links.write(space)

#     os.system(f"awk '!x[$0]++' {search_query}_daily.txt > {search_query}_temp.txt")

#     file_all_links.close
#     # temp_new_links.close


# Dictionary inplementation------------------------------------------------------

# categories_id = {}

# collection_name = input("Enter the username you want to add :")
# collection_id = input("Enter the collection ID:")

# print(collection_name)
# print(collection_id)

# categories_id[collection_name] = collection_id

# get_collection = input("Enter the collection you would like to get:")

# # print(categories_id(f"{get_collection}"))
# print(categories_id[get_collection])


# Json Implementation ------------------------------------------------------------

import json


# search_query = input("Enter the search query:")

# collection_name = input("Enter the name you want to call this :")
# collection_username = input("Enter the username :")
# collection_id = input("Enter the collection ID :")


# Reading Json ------------

import json

file = open("wallheaven_collection.json", "r")

content = file.read()
wallpaper_sfw = json.loads(content) #sfw walls
wall_json_sfw = wallpaper_sfw['sfw_collection'] #using json and extracting the data var
image_link_sfw = (wall_json_sfw[1]['collection_name'])     #link to random sfw wallpaper
        
return image_link_sfw

file.close()