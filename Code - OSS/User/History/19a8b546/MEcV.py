  
  
  
  
  
  
  
  
      if k == 1:
        wallpaper_sfw = json.loads(wallpaper_Sfw_Api.text) #sfw walls
        wall_json_sfw = wallpaper_sfw['data'] #using json and extracting the data var
        image_link_sfw = (wall_json_sfw[x]['path'])     #link to random sfw wallpaper
        # 
        return image_link_sfw

    elif k == 2:
        wallpaper_Nsfw = json.loads(wallpaper_Nsfw_Api.text) #nsfw walls    
        wall_json_nsfw = wallpaper_Nsfw['data']
        image_link_nsfw = (wall_json_nsfw[x]['path'])   #link to random nsfw wallpaper

        return image_link_nsfw
    else:
        print("Error 404")