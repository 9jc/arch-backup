import json, os, re
os.system("clear||cls")

# Loads the json data ---- 
jsonData = open('/home/i0xfce/MEGAsync/Projects/Python/wallheaven_collection.json', "r")
# reads the json data
data_read = jsonData.read()
data_load = json.loads(data_read)

# parsinng the general data list
wall_json_sfw_collection = data_load['nsfw_collection']
# checking the index of x_colllection --- 
index_json  = [index for (index, item) in enumerate(wall_json_sfw_collection)]

# looping through the index x_collection --- 
for item in index_json:
    x = item

    wall_json_sfw_collection1 = wall_json_sfw_collection[x]["collection_name"]

    # Searching the valude of user input to see if its already there --- 
    val = 'Mature-21' in wall_json_sfw_collection1 # Returns Bool
    val_str = str(val) # Converting to string so that file can write it
    space = " ," 

    # Writing it into a temp file for checking later --- 
    file = (open("temp.txt", "a"))
    file.write(val_str)
    file.write(space)
    file.close()

# Checking if the user value exist 

# opening the previous temp file in read mode
check_file = (open("temp.txt", "r"))
ddr = check_file.readline()

# using regx to check if the value already exist
res = bool(re.search("True", ddr)) # will return bool
if res == True:
    print("yes")
    pass
elif res == False:
    print("no")
    pass

# clearing the existing temp file 
clear_file = open('temp.txt', 'r+')
clear_file.truncate(0)
check_file.close()

# Done----------------------------------------
    

