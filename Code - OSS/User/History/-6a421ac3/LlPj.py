import json, os, re

os.system("clear||cls")


jsonData = open('/home/i0xfce/MEGAsync/Projects/Python/wallheaven_collection.json', "r")

data_read = jsonData.read()
data = json.loads(data_read)

wall_json_sfw_collection = data['nsfw_collection']



aio  = [index for (index, item) in enumerate(wall_json_sfw_collection)]
# print(aio) #----------------------------- gets the index of the json


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
print(ddr)
    
    
    # print(wall_json_sfw_collection1)



x = 'nsfw_collection' in data # returns False 
seriu = 'Mature-1' in wall_json_sfw_collection1 # returns False
    
# print(wall_json_sfw_collection1)
# print(seriu)




#--------------------------
# for item in aio:
#     n = item
#     # for b in range(0, n):
#     wall_json_sfw_collection1 = wall_json_sfw_collection[n]["collection_name"]
#     # print(wall_json_sfw_collection1)

#     # wall_json_sfw_collection3 = set(wall_json_sfw_collection1)
#     # print(wall_json_sfw_collection3)



#     x = 'nsfw_collection' in data # returns False
    
#     s = 'Bloncdccdwde-06' in wall_json_sfw_collection1 # returns False
#     # test_list1 = str(s)
#     # test_list2 = list(test_list1)
#     # test_list3 = str(test_list2)

#     xxx = test_list1

#     test_list = list(test_list1)
#     # print(test_list1)

#     res = bool(re.search("T", test_list3))
#     if res == True:
#         print("yes")
#         exit()
#     elif res == False:
#         pass
#         # print("no")
# print("wow")--------------



    # print(x)

    # if s == True:
    #     is_found = True
    #     # print("in the list")
    # elif s == False:
    #     is_found = False
    #     # print("Not in list")
    # else:
    #     print("failed")
    #     # print("not there ------")

# if is_found == True:
#     print("Bad")
# elif is_found == False:
#     print("Good")





