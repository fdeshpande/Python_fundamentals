# There are various functions of list:

'''List sort()'''
# This function is used to sort the list.
print("----:LIST SORTING METHOD:----")
F=[98,45,3,456,78,12,32,43,36,64,87,66,19,0,88]
print("Unsorted List:\t",F)
F.sort()
print("Sorted List :\t",F)

'''List Reverse()'''
# This function is used to reverse the list .
print("----:LIST REVERSINGING METHOD:----")
F=[98,45,3,456,78,12,32,43,36,64,87,66,19,0,88]
print("Initial List:\t",F)
F.reverse()
print("The reverse list is :\t",F)

'''List Append()'''
# This function is used to add any element or item at end in a list.
print("----:LIST APPEND METHOD:----")
F=[98,45,3,456,78,12,32,43,36,64,87,66,19,0,88]
print("Initial List:\t",F)
F.append(235)
print("The list after performing append mtd with 235 num:\t",F)

'''List Insert()'''
# This function is used to Insert any element or item at perticular index in a list.
print("----:LIST INSERT METHOD:----")
F=[98,45,3,456,78,12,32,43,36,64,87,66,19,0,88]
print("Initial List:\t",F)
F.insert(2,60)  #List.insert(index value,element)
print("The updated list is :\t",F)

'''List pop()'''
# This function is used to Delete any element or item at perticular index in a list.
print("----:LIST POP METHOD:----")
F=[98,45,3,456,78,12,32,43,36,64,87,66,19,0,88]
print("Initial List:\t",F)
F.pop(9)  #List.pop(index value)
print("The updated list after deleting element at index 9 is :\t",F)

'''List Remove()'''
# This function is used to remove any element or item in a list.
print("----:LIST REMOVE METHOD:----")
F=[98,45,3,456,78,12,32,43,36,64,87,66,19,0,88]
print("Initial List:\t",F)
F.remove(78)  #List.remove(element)
print("The updated list is after removing 78 element :\t",F)