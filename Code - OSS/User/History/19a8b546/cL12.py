for m in range(6, 34):
    text = str(m)
    line_breaker = "---------------------------------------------------------------------------"
    file = open("wall.txt", ("a"))
    space = ('\n')

    file.write(line_breaker)
    file.write(text)
    file.write(space)

    lines_seen = set() # holds lines already seen
    outfile = open("all_nsfw_links.txt", "w")
    for line in open("nsfw_wall_daily.txt", "w"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()

    file.close