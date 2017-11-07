"""write a program that read the words in any text file"""
filename = input("please enter file's name:", )
fh = open(filename)

"""build the dictionay, named "searchword" """
searchword = dict()
for line in fh:
    words = line.split()
    for word in words:
        searchword[word] = searchword.get(word,0) + 1

"""use the "in" operator as a fast way to check whether a string is in the dictionary."""
checkword = input('Enter a word to check:')
if checkword in searchword:
    print('got it', searchword[checkword])
else:
    print('not in it!')
