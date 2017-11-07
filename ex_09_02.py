fname = input('Please enter the file name:')
if len(fname)<1: fname = 'mbox-short.txt'
fhand = open(fname)

wcount = dict()
for line in fhand:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
#look for the 3rd word
        day = words[2]
#running count of each of the days of the week
        wcount[day] = wcount.get(day, 0) +1
print(wcount)
