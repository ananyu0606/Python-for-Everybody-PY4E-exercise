num = 0
tot = 0.0
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

#check point
#print('ALL DONE')
print('Total:', tot, 'Count:', num, 'Average:', tot/num)
