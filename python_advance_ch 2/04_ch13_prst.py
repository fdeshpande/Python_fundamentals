''' Write a program to find the maximum of the numbers in a list using a reduce function.'''
from functools import reduce

l = [4,6,8,0,1,2,4]
a = reduce(max,l)
print(a)