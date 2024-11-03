'''Write a program to find whether a given username contains 10 characters or not'''

userName = input("Enter your username of 10 charcters:\t")
print(userName)
if(len(userName)==10):
    print("Entered username is valid.")
else:
    print("Please enter valid username of 10 character. ")