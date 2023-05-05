import datetime

date_now = datetime.datetime.now()

date1 = (date_now.strftime("%x"))
time1 = (date_now.strftime("%X"))
micro_sec = (date_now.strftime("%f"))


# search_query = input("Enter a name :")
search_query = "ll"

global line_breaker
line_breaker = f"{micro_sec}[ {search_query} | Date ~ {date1} - {time1} ] \n"
file_all_links = open(f"{search_query}_daily.txt", ("a"))
temp_new_links = open(f"{micro_sec}-{search_query}_temp.txt", ("w"))
for m in range(10, 200):
    text = str(m)
    
    space = ('\n') 
    
    file_all_links.write(text)
    temp_new_links.write(text)

    uniqlines = set(open(f'{search_query}_daily.txt').readlines())
    bar = open(f'{search_query}_all_links.txt', 'w').writelines(uniqlines)

    # outfile.write(line_breaker)
    # print(file)

    file_all_links.close
    temp_new_links.close