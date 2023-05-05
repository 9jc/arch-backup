
import json
import os
import re

def add_collection():

    # Asking Collection Details
    os.system("clear||cls")
    collection_name = input("Enter a name for the new collection:")
    collection_url = input("Enter the collection's url:")

    # Striping Username out of Url
    collection_username_1 = collection_url.replace("https://wallhaven.cc/user/", "") # Replacing First Part
    strip_username = re.search("/", collection_username_1) # searching for "/" character in collection_username_1
    bad_username_part = slice(strip_username.start()) #slicing after "/" part
    wallheaven_username = collection_username_1[bad_username_part] # Final Username from url after slicing

    print(wallheaven_username)

    # Striping Collection ID out of url
    collection_id_1 = collection_url.replace(f"https://wallhaven.cc/user/{wallheaven_username}/favorites/", "") # Replacing First Part
    strip_id = re.search("\?", collection_id_1) # searching for "/" character in collection_username_1
    bad_id_part = slice(strip_id.start()) #slicing after "/" part
    wallheaven_collection_id = collection_id_1[bad_id_part] # Final Username from url after slicing

    print(wallheaven_collection_id)


    # Asking if the collection is Nsfw / sfw
    collection_type_ask = input("Is it an sfw/nsfw collection :")
    
    if collection_type_ask == 'sfw':
        print(collection_type_ask)
    elif collection_type_ask == 'nsfw':
        print(collection_type_ask)
    else:
        print("Invalid Option detected!! type 'sfw' / 'nsfw' ")
        add_collection()
add_collection()

# https://wallhaven.cc/user/Dasert/favorites/209296?purity=110

# collection_username_1 = collection_url.replace("https://wallhaven.cc/user/", "") # Replacing First Part
# strip_username = re.search("/", collection_username_1) # searching for "/" character in collection_username_1
# bad_username_part = slice(strip_username.start()) #slicing after "/" part
# wallheaven_username = collection_username_1[bad_username_part] # Final Username from url after slicing

# print(wallheaven_username)

# collection_id_1 = collection_url.replace(f"https://wallhaven.cc/user/{wallheaven_username}/favorites/", "") # Replacing First Part
# strip_id = re.search("\?", collection_id_1) # searching for "/" character in collection_username_1
# bad_id_part = slice(strip_id.start()) #slicing after "/" part
# wallheaven_collection_id = collection_id_1[bad_id_part] # Final Username from url after slicing

# print(wallheaven_collection_id)
# print(collection_type)



#-------------------------------------------
# # function to add to JSON - https://www.geeksforgeeks.org/append-to-json-file-using-python/
# def write_json(new_data, filename='/home/i0xfce/MEGAsync/Projects/Python/wallheaven_collection.json'):
#     with open(filename,'r+') as file:
#         # First we load existing data into a dict.
#         file_data = json.load(file)
#         # Join new_data with file_data inside emp_details
#         file_data["nsfw_collection"].append(new_data)
#         # Sets file's current position at offset.
#         file.seek(0)
#         # convert back to json.
#         json.dump(file_data, file, indent = 4)
 
#     # python object to be appended
# y = {
#     "collection_name": collection_name,
#     "username": wallheaven_username,
#     "collection_id": wallheaven_collection_id,
#     "collection_url": collection_url
#     }
     
# write_json(y)