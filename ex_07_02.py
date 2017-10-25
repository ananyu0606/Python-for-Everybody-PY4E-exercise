# Use the file name mbox-short.txt as the file name
while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname)
        break
    except:
        print('file not found:', fname)
        continue

total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    position = line.find(':')
    linenumber = line[20:]
#    print(line)
#    print(position)
#    print(linenumber)
    floatnumber = float(linenumber)
    total = total + floatnumber
    count = count + 1

#print('total:', total)
print('Average spam confidence:', total/count)
#print("Done")
