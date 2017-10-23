num = 0
tot = 0.0
maxnum = None
minnum = None

while True :
    sval = input ('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue

    #check point
    #print(fval)
    num = num + 1
    tot = tot + fval

    if maxnum is None or fval > maxnum:
        maxnum = fval
    #check point
    #print('current MAX: ', maxnum)
    if minnum is None or fval < minnum:
        minnum = fval
    #check point
    #print('current min: ', minnum)

#check point
#print('ALL DONE')
#print('Total: ', tot)
#print('Count: ', num)
#print('Average ', tot/num)
print('Maximum is', int(maxnum))
print('Minimum is', int(minnum))
