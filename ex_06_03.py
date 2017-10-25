def count(string, letter):
    count = 0
    for i in string:
        if i == letter:
            count += 1
    return count

inputstring = input('Enter a tring: ')
assignletter = input('Assign a letter: ')
outcome = count(inputstring, assignletter)
print('count the letter in string:', outcome)
