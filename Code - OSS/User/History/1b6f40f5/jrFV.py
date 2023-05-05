ask_user_to_download = input("Do you want to download the images(2) / quit(1) ? ")
if ask_user_to_download == "1":
    program_start()
elif ask_user_to_download == "2":
    res = requests.get(image_link_nsfw, stream = True)
    file_name = f"{search_query}_{micro_sec}_wall.jpeg"
#             
#       
    # Downloading image and checking if the response code is 200
    # if res.status_code == 200:
    with open(file_,'wb') as f:
        shutil.copyfileobj(res.raw, f)
    print('Image sucessfully Downloaded: ',file_name)
    time.sleep(3)
    # else:
    #     print('Image Couldn\'t be retrieved')