'''Write a python functio to print a multiplication table of  a given number:'''

num = int(input("Enter any number:\t"))
def table():
    print(f"The of entered number {num} is:\t\n")
    for i in range(11):
            
        print(f"{num} x {i} = {num * i}")

table()