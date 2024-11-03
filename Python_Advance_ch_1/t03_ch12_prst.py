'''Write a list comprehension to print a list which contain the multiplication 
table of a user entered number..'''

a = int(input("Enter any number :\t"))
l = [a*i for i in range(1,11) ]
print(l)
