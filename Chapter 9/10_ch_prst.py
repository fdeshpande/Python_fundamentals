'''Write a program to rename a file to 'renamed_by_python.txt' '''
import os

oldname = 'sample2.txt'
newname = 'renamed_by_python.txt'

with open(oldname) as f:
    u = f.read()
with open(newname , 'w') as f:
    f.write(u)

os.remove(oldname)       