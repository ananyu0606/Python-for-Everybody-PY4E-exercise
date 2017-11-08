fname = input('please enter teh file name:')
fhand = open(fname)

wcount = dict()
for line in fhand:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
#pull the hour out from the 'From ' line by finding the time
        time = words[5]
#splitting the string a second time using a colon.
        timesplit = time.split(':')
        hour = timesplit[0]
#running count of each "hour"
        wcount[hour] = wcount.get(hour, 0) +1

# print out the counts, sorted by hour
tem = list()
for k,v in wcount.items():
    newpair = (k, v)
    tem.append(newpair)
result = sorted(tem)
#print(result)

for counthour in result:
    print(counthour[0], counthour[1])
