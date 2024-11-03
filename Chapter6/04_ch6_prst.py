# Write  a program to find greatest of four numbers entered by user.

a1 = int(input("Enter first num:\t"))
a2 = int(input("Enter second num:\t"))
a3 = int(input("Enter third num:\t"))
a4 = int(input("Enter fourth num:\t"))

a = [a1,a2,a3,a4]
print(" The four num are: \t\n",a)
if(a1>a2):
    f1 = a1
else:
    f1 = a2

if(a3>a4):
    f2 = a3
else:
    f2 =a4

if(f1>f2):
    print("greater num is:\t",f1)
else:
    print("greater num is:\t",f2)


