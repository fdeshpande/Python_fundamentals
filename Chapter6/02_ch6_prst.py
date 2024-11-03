'''Write a program to print yess when the age entered 
by the user is greater than or equal to 18 by using logical operator'''

userAge = int(input("Enter your age :\t"))
print(userAge)
if(userAge>= 18 and userAge <=40):
    print("Yess , You are eligible.")
else:
    print("No,You are not eligible.")

