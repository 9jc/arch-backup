import json, os, re, time
# from _add_collections import collection_name as name


# os.system("clear||cls")

temp_file_name = (open("/home/i0xfce/MEGAsync/Projects/Python/Wallpaper_Downloader/temp/temp1.txt", "r"))
temp_read_name = temp_file_name.readline()
print(temp_read_name)
#

def value_exist_check(k):
    # Loads the json data ---- 
    jsonData = open('/home/i0xfce/MEGAsync/Projects/Python/Wallpaper_Downloader/temp/wallheaven_collection.json', "r")
    # reads the json data
    data_read = jsonData.read()
    data_load = json.loads(data_read)

    # parsinng the general data list
    wall_json_collection_1 = data_load['nsfw_collection']
    # checking the index of x_colllection --- 
    index_json  = [index for (index, item) in enumerate(wall_json_collection_1)]

    # looping through the index x_collection --- 
    for item in index_json:
        x = item

        wall_json_collection_2 = wall_json_collection_1[x]["collection_name"]

        # Searching the valude of user input to see if its already there --- 
        check_value = temp_read_name in wall_json_collection_2 # Returns Bool
        check_value_str = str(check_value) # Converting to string so that file can write it
        space = " ," 

        # Writing it into a temp file for checking later --- 
        file = (open("/home/i0xfce/MEGAsync/Projects/Python/Wallpaper_Downloader/temp/temp.txt", "a"))
        file.write(check_value_str)
        file.write(space)
        file.close()

    # Checking if the user value exist 

    # opening the previous temp file in read mode
    temp_file = (open("/home/i0xfce/MEGAsync/Projects/Python/Wallpaper_Downloader/temp/temp.txt", "r"))
    temp_read = temp_file.readline()

    global res
    # using regx to check if the value already exist
    res = bool(re.search("True", temp_read)) # will return bool

    clear_file = open('/home/i0xfce/MEGAsync/Projects/Python/Wallpaper_Downloader/temp/temp.txt', 'w')

    if k == 1:
        return False

    return False

    # if res == True:
    #     # os.system("clear||cls")
    #     # print("Collection Name already taken, Please try another...")
    #     # time.sleep(5)
    #     return "True"
    #     pass
    # elif res == False:
    #     return "False"
    #     pass

    # clearing the existing temp file 
    clear_file = open('/home/i0xfce/MEGAsync/Projects/Python/Wallpaper_Downloader/temp/temp.txt', 'w')
    print(res)

# value_exist_check()
xc = 1
if xc == 1:
    value_exist_check()
    print(xio)

# Done----------------------------------------
    

