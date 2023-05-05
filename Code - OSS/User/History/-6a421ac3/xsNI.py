import json, os, re
os.system("clear||cls")


def value_exist_check():
    # Loads the json data ---- 
    jsonData = open('/home/i0xfce/MEGAsync/Projects/Python/wallheaven_collection.json', "r")
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
        check_value = 'Mature-1' in wall_json_collection_2 # Returns Bool
        check_value_str = str(check_value) # Converting to string so that file can write it
        space = " ," 
    
        # Writing it into a temp file for checking later --- 
        file = (open("temp.txt", "a"))
        file.write(check_value_str)
        file.write(space)
        file.close()
    
    # Checking if the user value exist 
    
    # opening the previous temp file in read mode
    temp_file = (open("temp.txt", "r"))
    temp_read = temp_file.readline()
    
    # using regx to check if the value already exist
    res = bool(re.search("True", temp_read)) # will return bool
    if res == True:
        print("yes")
        pass
    elif res == False:
        print("no")
        pass
    
    # clearing the existing temp file 
    clear_file = open('temp.txt', 'r+')
    clear_file.truncate(0)
    temp_file.close()

# Done----------------------------------------
    

