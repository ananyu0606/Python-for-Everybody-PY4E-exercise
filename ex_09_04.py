fname = input('please enter teh file name:')
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
#print(wcount)

maxcount = -1
mostsent = None
for key, value in wcount.items():
    if value > maxcount:
        maxcount = value
        mostsent = key #capture the key
print(mostsent, maxcount)
