'''Write a program to read the text from a given file . poem.txt 
and findout whether it contains the word 'Twinkle' '''

file = open('poem.txt','r') #open the file in read mode
data = file.read()  
if 'Twinkle' in data: 
    print("Twinkle is present")
else:
    print("Twinkle is not present")

file.close()