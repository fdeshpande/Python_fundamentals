'''Write a program to convert inches into centimeter:'''

inch = int(input("Enter any value to convert into centimeter:\t"))
 
def convert_i_c():
    cm = inch*2.54
    print(f"The converted value from inches to centimeter is:\t{cm} cm")

convert_i_c()