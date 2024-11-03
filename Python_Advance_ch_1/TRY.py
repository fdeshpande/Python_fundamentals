'''We can also specify the exception to catch like below . '''

try:
    a = int(input("Enter a number :\t"))
    c = 1/a
    print(c)

except ValueError as e :
    print("Please enter a valid numeral....")

except ZeroDivisionError as e :
    print("make sure you are not dividing by 0 ... ")

print("Thanks for using this code ....")    