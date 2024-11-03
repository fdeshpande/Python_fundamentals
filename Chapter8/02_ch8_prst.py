'''Write a program to convert celcius to fahrenheit using function:
Basic formula :    c/5 = (f-32)/9
                         or
                         (9c/5)+32 = f '''

temp = int(input("Enter any centigrade / celcius value to convert into fahrenheit:\t"))
 
def convert_c_f():
    f = 32 + (9*temp/5)
    print(f"The converted value of temperature from celcius to farhenheit is:\t{f} *F")

convert_c_f()

