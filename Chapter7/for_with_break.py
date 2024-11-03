# break is used to come out of the loop when encountered ...
# It instruct the program to exit the loop now.

for i in range(10):
    print(i)
    if i==3:
        break
else: # else statement runs when loop is excuting or terminating naturally not forcefully.
    print("Done") 
