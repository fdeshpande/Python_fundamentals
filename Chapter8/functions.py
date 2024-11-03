'''Function is group of statement performing a specific task.
 The part of instruction which are executed during the function call.'''

 #Write a program to greet a user with "Good day " using function:


def greet(name):
    print("Have a good day , "+name)

greet("Falguni")    
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# function with argument:
def sum(n1 ,n2):
    print(n1+n2)

sum(4,5)    

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# function without argument:
def sum():
    a1 = 20 
    a2 = 40
    a = a1 + a2
    print(a)
sum()    
