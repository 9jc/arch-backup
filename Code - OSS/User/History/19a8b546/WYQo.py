for m in range(1, 24):
    text = str(m)
    file = open("wall.txt", ("a"))
    space = ('\n')

    file.write(m)
    file.write(space)

    lines_seen = set() # holds lines already seen
    outfile = open("out.txt", "w")
    for line in open("wall.txt", "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()

    file.close