'''Write a program to print yess when the age entered 
by the user is greater than or equal to 18'''

requiredAge = 18
userAge = int(input("Enter your age :\t"))
print(userAge)
if(userAge >= requiredAge):
    print("Yess , Tum bade ho gaye ho!!!!!")
else:
    print("No,Pehle bade ho jao")
