# random numbers are inserted throughout the text
#The numbers can appear anywhere in the line. There can be any number of numbers in each line (including none)
#cauculate the sum of these numbers

import re
fhand = open('regex_sum_41758.txt')
number = []
count = 0
for line in fhand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        number = number+x
#print(number)

total = 0
for item in number:
    item = int(item)
    total = total + item
    count += 1
#print(count)
print(total)
