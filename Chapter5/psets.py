'''Set is collection of non repetative item.
Sets are unordered.
Sets are unindexed.
Empty set can be created using syntax: b=set() .
There is no way to change item in sets.
set can contain duplicate values.
we can not add list or dictionary in set because they are mutable and hashable while sets are immutable ,
If we add list or dict into a sets then we can modify the list or dict which would be voilation of set creation in python.
we can add tuples into sets ,both are immutable and unhashable.'''

#Creation of set:

s ={1,2,3,4,5,6,2}
print(s) # prints the non repetated values.
print(type(s))

s1 = {} # always seems like a empty dict /wrong way to creation of empty set.
print(type(s1))

a = set() # correct way to create an empty set.
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
