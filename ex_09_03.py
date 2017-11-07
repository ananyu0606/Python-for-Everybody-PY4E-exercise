fname = 'mbox-short.txt'
fhand = open(fname)

wcount = dict()
for line in fhand:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
#look for the address
        address = words[1]
#running count of each mail address
        wcount[address] = wcount.get(address, 0) +1
print(wcount)

#print in pairs
for key in wcount:
    print(key, wcount[key])
