'''Write a program using function to find greater of three numbers: '''

a = int(input("Enter first num:\t"))
b = int(input("Enter second num:\t"))
c = int(input("Enter third num:\t"))

def greaterNum():
    if a>=b:
        g1 = a
    else:
        g1 = b

    if g1>=c:
        g2 = g1
    else:
        g2 = c
    print("The greater number is :\t",g2)

greaterNum()                    
