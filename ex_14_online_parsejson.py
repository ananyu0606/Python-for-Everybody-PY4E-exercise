import urllib.request, urllib.parse, urllib.error
import json

dataurl = input('Enter loaction: ')
print('Retrieving', dataurl)

urlhandler = urllib.request.urlopen(dataurl)
data = urlhandler.read() #read the content
print('Retrieved', len(data), 'characters')

#print(data)

info = json.loads(data)
#print('User count:', len(info))
namelist = info['comments']
count = list()
for item in namelist:
    count.append(item['count'])
    #print('count', item['count'])
print(sum(count))
