import datetime
import os

date_now = datetime.datetime.now()

date1 = (date_now.strftime("%x"))
time1 = (date_now.strftime("%X"))
micro_sec = (date_now.strftime("%f"))


# search_query = input("Enter a name :")
search_query = "ll"

global line_breaker
line_breaker = f"{micro_sec}[ {search_query} | Date ~ {date1} - {time1} ] \n"
file_all_links = open(f"{search_query}_daily.txt", ("a"))
# temp_new_links = open(f"{search_query}_temp.txt", ("w"))
for m in range(10, 600):
    text = str(m)
    
    space = ('\n') 
    
    file_all_links.write(text)
    file_all_links.write(space)

    os.system(f"awk '!x[$0]++' {search_query}_daily.txt > {search_query}_temp.txt")


    # temp_new_links.write(space)
    # temp_new_links.write(text)

    # outfile.write(line_breaker)
    # print(file)

    file_all_links.close
    # temp_new_links.close