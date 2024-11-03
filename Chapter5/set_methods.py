'''--:Set Methods:--'''

from tkinter import N
from turtle import clear


s1 = {} # always seems like a empty dict /wrong way to creation of empty set.
print(type(s1))

print("---:SET ADD():---")
a = set() # corret way to create an empty set.
print(type(a))
a.add(2)  # in set we use the add function to push elements into set.
a.add(4)
a.add(5)
a.add(6)
a.add(7)
a.add(8)
a.add(9)
a.add(4)
a.add((56,66,76)) # added a tuple in set.
print(a)

print("---:SET LEN():---")
print(len(a)) # it gives the length of set.

print("---:SET remove():---")
print(a.remove(7)) # it gives the updated set after removing 7 from set only If 7 is present in a set.otherwise it will give an error.
print(a)

print("---:SET POP():---")
print(a.pop()) # it gives the updated set after popping any element which is on top from set.
print(a)

print("---:SET UNION():---")
print(a.union({33,51})) # it gives the updated set after performing union in set.

print("---:SET INTERSECTION():---")
print(a.intersection({33})) # it gives the updated set after performing intersection in set.

print("---:SET CLEAR():---")
print(a.clear()) # it clear the set.





