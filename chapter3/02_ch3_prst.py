# Write a program to fill in a letter template given below with name and date.

letter = '''Dear <Name>,
hey happy to inform you that your skills are matched with our requirement .
have a good day !
You are Selected !
Thanks and regards
Jorjie
Date :<DATE>'''
name = input("Enter your name\n")
date = input("Enter date\n")
letter =letter.replace('<Name>',name)  
letter =letter.replace('<DATE>',date)
print(letter)             