'''Write a program to greet all the person names stored in a list l1 and which starts with 'S'...'''

nameList = ['Harry','Soham','Sachin','Rahul']
for name in nameList:
    if name.startswith('S'):
        print("Hello\t"+str(name))