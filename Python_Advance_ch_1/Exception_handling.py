'''There are many buildin exception in python when something goes wrong .
Exception in python handled by using try statement using python .
The code that hamdles the exception is written in exception clauses. '''

while (True):
    print("press q to quit...")
    a = int(input("Enter the number : "))

    if a == 'q' :
        break
    try:
        if a>6:
            print("You entered a number greater than 6 .")
    except Exception as e:
        print(f"Your input resulted in an error {e}")

print("Thank you for playing this game...")
