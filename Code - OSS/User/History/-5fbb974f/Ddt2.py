import requests
import os
import json
import random
import time
import webbrowser
import datetime
import requests 

from _secrets_ import *
from _messages_ import *
from _download_ import *
from config import * 


def wallpaper_fun(k):    
    # Wallpaper APi URL
    # wallpaper_no_Api = requests.get(f"https://wallhaven.cc/api/v1/search?q={search_query}&categories={wall_categories}&purity={purity_level}&atleast={wall_resolution}&ratios={ratios_type}&topRange={date_range}&sorting={sorting_info}&order=desc&page={page_no}")
    wallpaper_search_Api = requests.get(f"https://wallhaven.cc/api/v1/search?q={search_query}&categories={wall_categories}&purity={purity_level}&atleast={wall_resolution}&ratios={ratios_type}&topRange={date_range}&sorting={sorting_info}&order=desc&page={page_no}&apikey={API_KEY_WALLHEAVEN}")
    # wallpaper_collection_Api = requests.get(f"https://wallhaven.cc/api/v1/collections/{wallheaven_username}/{collection_id}?categories={wall_categories}&purity={purity_level}&atleast={wall_resolution}&ratios={ratios_type}&topRange={date_range}&sorting={sorting_info}&order=desc&page={page_no}&apikey={API_KEY_WALLHEAVEN}")

    # numbers wall
    # wall_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]

    # making a random cho1ise o1f wall number list
    # wall_number_random = random.choice(wall_numbers) 
    # x = int(wall_number_random) # converting str to int

    # print(wallpaper_no_Api)
    print("--------------------")
    print(wallpaper_search_Api)
    print("--------------------")
    # print(wallpaper_collection_Api)
    # type_fw = "1"
    
    # wall_type2 = int(type_fw)

    if k == 1:
        print("reached k =1 ")

        wallpaper_sfw = json.loads(wallpaper_no_Api.text) #sfw walls
        wall_json_sfw = wallpaper_sfw['data'] #using json and extracting the data var
        image_link_sfw = (wall_json_sfw[x]['path'])     #link to random sfw wallpaper
        
        return image_link_sfw

    elif k == 2:
        print("reached k =2 ")
        

        time.sleep(2)
        wallpaper_Nsfw = json.loads(wallpaper_search_Api.text) #nsfw walls  
        # print(wallpaper_Nsfw)  s
        wall_json_nsfw = wallpaper_Nsfw['data']
        # print(wall_json_nsfw)
        for x in range(1, 24):
            try:            
                image_link_nsfw = (wall_json_nsfw[x]['path'])   #link to random nsfw wallpaper
                save_file = open(f"/home/i0xfce/MEGAsync/Projects/Python/Wallpaper_Downloader/Links/{search_query}_daily.txt", ("a"))

                line_breaker = f"-----------------------------------{micro_sec}[ {search_query} | Date ~ {date1} - {time1} ] -------------------------------------\n"
                space = ('\n') 

                print(line_breaker)
                print(image_link_nsfw)

                # save_file.write(line_breaker)
                save_file.write(image_link_nsfw)
                save_file.write(space)
                print(space)

                # Removes duplicates and keeps only orginals
                os.system(f"awk '!x[$0]++' /home/i0xfce/MEGAsync/Projects/Python/Wallpaper_Downloader/Links/{search_query}_daily.txt > /home/i0xfce/MEGAsync/Projects/Python/Wallpaper_Downloader/Links/{search_query}_temp.txt")



                # Preview the images
                ask_user = input(f"Do you want to preview these images ? \n {image_link_nsfw} \n Avaliable Options - no/n / yes/y / q - quit ")
                if ask_user == "no" or ask_user == "n":
                    program_start()
                elif ask_user == "yes" or ask_user== "y" :
                    webbrowser.open(image_link_nsfw, new=2)
                    time.sleep(3)
                elif ask_user == "q":
                    exit()
                    
                
                # Download images
                ask_user_2 = input("Do you want to download all the images :")
                ask_user_3 = input("Do you want to apply the images :")


                if ask_user_2 == "yes" or ask_user_2 == "y":
                    download_img(url_image=image_link_nsfw, search_query=search_query, apply_wall=ask_user_3)
                    time.sleep(3)
                else:
                    print("Unknown option quitting")
                # if preview_image == 'r':
                #     program_start()
                # else:
                #     webbrowser.open(image_link_nsfw, new=2)

            except KeyboardInterrupt:
                add_cursor()
                exit(1)

            except:
                print("Error 404")

    

# Validating wallpaper search
def validating_search_query():

    try:
        os.system('cls||clear')
        validating_search_query = search_query.isalpha()
        if validating_search_query == True:
            print(search_query)
            print(validating_search_query)
            wallpaper_fun(k=2)
        elif validating_search_query == False:
            print(f"{red}\n \n Search Query is limited to one word, more than one word detected!!")
            time.sleep(4)
            program_start().normal_wall_modules()
    
    
    def program_start():
        os.system("clear||cls")
        user_start = input(intro)
        os.system("cls||clear")
    
        if user_start == '1':
            # Def Available Modules
            def normal_wall_modules():
    
                global normWall1
                normalwall = input(normWall)
                normalwall1 = int(normalwall)
                os.system("cls||clear")
    
                # global wallheaven_normal_search, wallheaven_nsfw_search, wallpaper_cave_search
                global search_query
                if normalwall1 == 1:
                    search_query = input(f"\n{yellow} {magenta} Enter the search term you want to get wallpapers of {red}➤ ")
                    validating_search_query()
                elif normalwall1 == 2:
                    search_query = input(f"\n{yellow}{magenta} Enter the nsfw search term you want to get wallpapers of {red}➤ ")
                    validating_search_query()
                elif normalwall1 == 3:
                    search_query = input(f"\n{yellow} {magenta}Enter the search term you want to search {red}➤ ")
                    f"\n {red} This Module is not yet ready!!"
    
                elif normalwall1 == 4:
                    help_menu = input(help_me) #prints the user help menu
                    os.system("cls||clear")
                    if help_menu == 'q':
                        exit()
                    else:
                        # print(error)
                        os.system("cls||clear")
                        normal_wall_modules()
    
                else:
                    print(error)
                    time.sleep(3)
                    os.system("cls||clear")
                    normal_wall_modules()
            normal_wall_modules()
    
        elif user_start == '2':
            print(f"\n {red} This Module is not yet ready!!")
            time.sleep(3)
            os.system("cls||clear")
            program_start()
        elif user_start == '3':
            exit()
        else:
            print(error)
            time.sleep(2)
            os.system("cls||clear")
            program_start()
    
    except:
        add_cursor()
        exit(1)

program_start()


# print(wallheaven_normal_search)
# print(wallheaven_nsfw_search)
# print(wallpaper_cave_search)



# # Wallpaper APi URL
# wallpaper_no_Api = requests.get(f"https://wallhaven.cc/api/v1/search?q={search_query}&categories={wall_categories}&purity={purity_level}&atleast={wall_resolution}&ratios={ratios_type}&topRange={date_range}&sorting={sorting_info}&order=desc&page={page_no}")
# wallpaper_search_Api = requests.get(f"https://wallhaven.cc/api/v1/search?q={search_query}&categories={wall_categories}&purity={purity_level}&atleast={wall_resolution}&ratios={ratios_type}&topRange={date_range}&sorting={sorting_info}&order=desc&page={page_no}&apikey={_API_KEY_WALLHEAVEN}")
# wallpaper_collection_Api = requests.get(f"https://wallhaven.cc/api/v1/collections/{wallheaven_username}/{collection_id}?categories={wall_categories}&purity={purity_level}&atleast={wall_resolution}&ratios={ratios_type}&topRange={date_range}&sorting={sorting_info}&order=desc&page={page_no}&apikey={API_KEY_WALLHEAVEN}")


