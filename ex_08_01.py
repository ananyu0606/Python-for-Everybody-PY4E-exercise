#removing the first and the last elements, and return None
def chop(t):
    t = t[1:-1]

#returns a new list that contains all but the first and last elemens
def middle(t):
    return t[1:-1]

letters = ['a', 'b', 'c', 'd', 'e', 'f']
cho = chop(letters) #returns None
mid = middle(letters) #new list
print(cho)
print(mid)
