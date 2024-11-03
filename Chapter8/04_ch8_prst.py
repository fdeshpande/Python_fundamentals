'''Write a reccursive function to calculate the sum of first n natural numbers:'''

n = int(input("enter any number:\t"))
def add(n):
    if n==0 or n==1:
        return 1
    else:
        return n +  add(n-1)  

a = add(n)
print(a)        
        