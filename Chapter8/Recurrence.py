'''Recurrence is a function which calls itself.
it is used to directly use a mathematical formula as function.'''

# factorial of any number using loop:

n = int(input("enter any number:\t"))
fact = 1
for i in range(n):
    fact = fact * (i+1)
print(fact)    
##############################################################################################
# factorial of any number using recurrence function:

n = int(input("enter any number:\t"))
def facto(n):
    if n==0 or n==1:
        return 1
    else:
        return n *  facto(n-1)  

a = facto(n)
print(a)        
        
    


     
   
