import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

dataurl = input('Enter loaction: ')
print('Retrieving', dataurl)

urlhandler = urllib.request.urlopen(dataurl)
data = urlhandler.read() #read the content
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
commentlst = tree.findall('.//comment') #Xpath selector
countcalculator = 0
totalsum = list()
for item in commentlst:
    countcalculator += 1
    number = item.find('count').text
    number = float(number)
    totalsum.append(number)

print('Count: ', countcalculator)
print('Sum: ', sum(totalsum))
