'''Lists are sequence datatype .
 In which we can store multiple values of different datatypes.
 List can be modified during run time .
 List can be represented in a square bracket.
 list is mutable.
'''
# List Creatinon:

F =['Falguni',22,'CSE','Graduated','batch-2021']
print(F)

# list Indexing:
'''List can be indexed just like a string .'''
print(F[2]) # it is printing the element of index 2.
print(F[4])
print(F[3])
print(F[1])
print(F[0])

#List Slicing:
print(F[1:4])
print(F[0::2])
F[1]= 'Twenty-Two'  # here we are modifing the list .
print(F)  # printing modified list.

