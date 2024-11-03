'''Write a program to open three files 1.txt , 2.txt , 3.txt .
If any of these files are not present , a msg without existing the program must be printed 
promting the same....'''

try: 
    with open('1.txt','r') as f:
        a = f.read()
        print(a) 


    with open('2.txt','r') as f:
        b = f.read()
        print(b)   

    with open('3.txt','r') as f:
        c = f.read()
        print(c)

except Exception as e:
    print(e)
    print("File is not present...")


print("**************************or***************************************")

def findfile(filename):
    try:
        with open(filename ,'r') as f:
            print(f.read())

    except FileNotFoundError as e:
        print(e)
        print(f"File {filename} is not found...")

findfile('1.txt')
findfile('2.txt')
findfile('3.txt')

