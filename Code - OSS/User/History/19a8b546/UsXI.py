import datetime

date_now = datetime.datetime.now()

date1 = (date_now.strftime("%x"))
time1 = (date_now.strftime("%X"))

search_query = input("Enter a name :")

line_breaker = f"--------------------------------[ {search_query} | Date ~ {date1} - {time1} ]------------------------------------ \n"
file = open(f"{search_query}_daily.txt", ("a"))
file.write(line_breaker)

for m in range(50, 200):
    text = str(m)
    
    space = ('\n') 
    
    file.write(text)
    file.write(space)

    lines_seen = set() # holds lines already seen
    outfile = open(f"all_{search_query}_links.txt", "w")
    outfile.write(line_breaker)
    for line in open(f"{search_query}_daily.txt", "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()

    file.close