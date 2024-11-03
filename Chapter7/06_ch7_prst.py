# write a program to check whether the entered number is prime or not:

num = int(input("Enter any number:\t"))

if num%1==0 and num%num ==0:
    print("The entered number is prime\t")
else:
    print("The number is not prime :\t")    