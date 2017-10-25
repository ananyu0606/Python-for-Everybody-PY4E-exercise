while True:
    fname = input('Enter the file name:')
    try:
        fhand = open(fname)
        break
    except:
     if fname == 'na na boo boo':
         print("NA NA BOO BOO TO YOU - You have been punk'd!")
         exit()
     if fname == 'stop':
         exit()
     print('File cannot be opened:', fname)
     continue

count = 0
for line in fhand:
    if line.startswith('Subject'):
        count += 1

print('There were', count, 'subject lines in', fname)
