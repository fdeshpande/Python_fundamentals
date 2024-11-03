'''Write a program to find whether a given name is present in a list or not.'''

nameList = ['Dishant','Amit','Falguni','Sumit','Himanshu','Chhavi']
Ename = input("Enter your name:\t")
print(Ename)
if(Ename in nameList):
    print("Name is found!!!")
else:
    print("Sorry!! not found . your name is not in our list.")    