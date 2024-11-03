'''Write a program to print third ,fifth , and seventh element from a list using 
enumerate function...'''
list = [3,53,2,False,6.4,'falguni',5,89,90,'love']
index = 0

for index ,item in enumerate(list):
    if index==2 or index==4 or index== 6:
        print(f"The {index+1}th element is {item}")
    