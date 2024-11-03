'''Write a program to remove a given word from a string and strip it at the same frame:'''

def nameStrip(string , word ):
    nam = string.replace(word ,"")
    return nam.strip()
    
this = "  falguni is beautiful    "
n = nameStrip(this , "falguni")
print(n)    