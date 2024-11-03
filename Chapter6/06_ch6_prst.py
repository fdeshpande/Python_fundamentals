# A spam comment is defined as a text containsing following keyword:
'''"make a lot of money","buy now","subscribe this","click this".Write a program to detect this spams'''

spamMsg = ["make a lot of money","buy now","subscribe this","click this"]
freeMsg = input("Enter any msg:\t")
print(spamMsg)
print(freeMsg)
if(freeMsg in spamMsg):
    print("This is spam msg ALERT!!!!!")
else:
    print("not a spam msg...have a good day!!!!")
    
   