import datetime

date1 = datetime.datetime,now()

name = input("Enter a name :")

for m in range(1, 314):
    text = str(m)
    line_breaker = f"--------------------------------[ {name} | Date ~ {date1.strftime(%x)} - {date1.strftime(%X)} ]------------------------------------ \n"
    file = open("nsfw_wall_daily.txt", ("a"))
    space = ('\n')

    file.write(line_breaker)
    file.write(text)
    file.write(space)

    lines_seen = set() # holds lines already seen
    outfile = open("all_nsfw_links.txt", "w")
    for line in open("nsfw_wall_daily.txt", "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()

    file.close