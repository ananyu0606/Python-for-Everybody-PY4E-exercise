"""8.4 Open the file romeo.txt and read it line by line."""

fname = input("Enter file name: ")
wordlist = []
fh = open(fname)

"""For each line, split the line into a list of words using the split() method.
The program should build a list of words."""
for line in fh:
    line = line.split()

    """For each word on each line check to see if the word is already in the list
    and if not append it to the list."""
    for words in line:
        if words in wordlist:
            continue
        wordlist.append(words)

"""When the program completes,
sort and print the resulting words in alphabetical order."""
wordlist.sort()
print(wordlist)
