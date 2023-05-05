import json, os, re

os.system("clear||cls")


jsonData = open('/home/i0xfce/MEGAsync/Projects/Python/wallheaven_collection.json', "r")

data_read = jsonData.read()
data = json.loads(data_read)

wall_json_sfw_collection = data['nsfw_collection']



aio  = [index for (index, item) in enumerate(wall_json_sfw_collection)]

for item in aio:
    n = item
    global wall_json_sfw_collection1
    wall_json_sfw_collection1 = wall_json_sfw_collection[n]["collection_name"]
    val = 'Mature-1' in wall_json_sfw_collection1
    val_str = str(val)
    space = " ,"


    file = (open("temp.txt", "a"))
    file.write(val_str)
    file.write(space)
    file.close()
    # print(val_str)

check_file = (open("temp.txt", "r"))
ddr = check_file.readline()
res = bool(re.search("True", ddr))
if res == True:
    print("yes")
    pass
elif res == False:
    print("no")
    pass

clear_file = open('temp.txt', 'r+')
clear_file.truncate(0)
    

