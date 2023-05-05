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

file = open("wallheaven_collection.json", "r") # opens json file in read mode

wallheaven_collection = file.read() # reads the json file
wallpaper_sfw_collection = json.loads(wallheaven_collection) # loads the json file
wall_json_sfw_collection = wallpaper_sfw_collection['sfw_collection'] # using json and extracting the data var
collection_date_sfw = (wall_json_sfw_collection[1]['collection_name']) # link to random sfw wallpaper
        
print(collection_date_sfw)

file.close()


# Adding New data to json file--------------------------------------------------------

# function to add to JSON
def write_json(new_data, filename='/home/i0xfce/MEGAsync/Projects/Python/wallheaven_collection.json'):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["nsfw_collection"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
 
    # python object to be appended
y = {
    "collection_name": "Mature-1",
    "username": "Dasert",
    "collection_id": "209296",
    "collection_url": "https://wallhaven.cc/user/Dasert/favorites/209296?purity=110"
    }
     
write_json(y)