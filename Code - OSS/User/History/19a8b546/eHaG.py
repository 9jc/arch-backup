for m in range(6, 34):
    text = str(m)
    file = open("wall.txt", ("a"))
    space = ('\n')

    file.write(text)
    file.write(space)

    lines_seen = set() # holds lines already seen
    outfile = open("out.txt", "w")
    for line in open("wall.txt", "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()

    file.close