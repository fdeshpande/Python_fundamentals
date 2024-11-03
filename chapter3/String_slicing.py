'''A string in python can be break into parts or sliced for getting a part of the string
by using following syntax :  "sl = name[index start: index end] "     
ex:   f  a  l  g  u  n  i    it means the string length is 7 or string can be start from 0 to (length -1)
      0  1  2  3  4  5  6 
     -7 -6 -5 -4 -3 -2 -1'''
# we cant change/update the element of string.
name = 'Falguni'
print(name[0])
print(name[6])
print(name[0:5])
print(name[1:5])
print(name[:5]) #it assume first index as 0.
print(name[0:]) # it assume to print full string.
# if we want to access last character from string then we use or negative index .
q = name[-4:-1]
print(q)

'''Slicing with skip value'''
# if we provide a skip value a a part of our slice like this , we must use a syntax like 
#syntax :  sl = name[starting index : ending index : step/skip index] 
# skip index is used to what element is going to skip while printing the string.

word = 'iampetloverilovepetsalots'
print(word[0::2])
print(word[0:5:3])