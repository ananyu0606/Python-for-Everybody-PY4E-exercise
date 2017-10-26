fname = input('Enter a file name:' )
fhand = open(fname)
for line in fhand:
    line = line.rstip()
    line = line.upper()
    print(line)
