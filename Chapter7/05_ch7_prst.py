'''Write a program to print multiplication table of a given number using while loop:'''

print("Please enter any number for which you are looking for a table:\t\n")
num = int(input("Enter any number:\t"))
i=0
while i<=10:
    print(f"{num}X{i}={num*i}")
    i = i+1
