'''Write a program to display a/b where both are integers . If b = 0 ,
 display infinite by handling the ZeroDivisionError.......'''

try:
    a = int(input("Enter any integer number:\t"))
    b = int(input("Enter second integer number for division:\t"))
    
    c = a/b
    print(f"value of a : {a}")
    print(f"value of b : {b}")
    print(c)
except ZeroDivisionError as e:
    print(e)
    print("value of 'b' should not be zero '0' ....please enter valid integer except 0 ...")


