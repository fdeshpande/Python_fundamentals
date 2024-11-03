'''Write a program to print multiplication table of a given number using for loop:'''

from audioop import reverse


print("Please enter any number for which you are looking for a table:\t\n")
num = int(input("Enter any number:\t"))
i=0
for i in range(11):
    table = num * i
    print(table)

    
