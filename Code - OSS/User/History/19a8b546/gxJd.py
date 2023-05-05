import datetime

date_now = datetime.datetime.now()

date1 = (date_now.strftime("%x"))
time1 = (date_now.strftime("%X"))
micro_sec = (date_now.strftime("%f"))


# search_query = input("Enter a name :")
search_query = "ll"

global line_breaker
line_breaker = f"{micro_sec}[ {search_query} | Date ~ {date1} - {time1} ] \n"
file = open(f"{search_query}_daily.txt", ("w"))

for m in range(10, 100):
    text = str(m)
    
    space = ('\n') 
    
    file.write(text)
    file.write(space)

    uniqlines = set(open(f'{search_query}_daily.txt').readlines())
    bar = open(f'{search_query}_daily_q.txt', 'w').writelines(uniqlines)

    # outfile.write(line_breaker)
    # print(file)

    file.close