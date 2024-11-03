# Assessment Question :

# Find the missing numbers from array
from array import *
arr = array('i',[3,6,7,8,10,13,17,19,20])
arr1 = array('i',[])
print('Input :',set(arr))
for i in range(arr[-1]+1):
    if i>= arr[0]:
        arr1.append(i)
print('Output :',list(arr1))


# Write a program to check whether the input character from the user is number or an alphabet .

input_ = input("Enter the character : ")
print("input : ",input_)
for i in input_:
    if ord('a')<= ord(i) <= ord('z') or ord('A')<= ord(i) <= ord('Z'):
        Output = 'Is alphabet'
    else:
        Output = 'Is number'
print("Output : ",Output)

# Write a program to switch the case of the starting letter of all words in a string sentence .

Input = 'he Ate an apple Under a Tree .'
Output = ''
l=[]
print("Input : ",Input)
for i in Input.split():
    a = i[0].swapcase()
    c = i.replace(i[0],a)
    l.append(c)
for i in l:
    Output = Output+" "+i
print("Output : ",Output)






