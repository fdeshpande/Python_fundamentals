'''Write a program to find the sum of first n naturals numbers using while loop...'''

l = [1,2,3,4]
i =0
while i<=len(l):
    sum= l[i] + l[i+1]
    print("The sum of first natural numbers are :\t",sum)
    i =i+1