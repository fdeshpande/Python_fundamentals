'''A file contains a word donkey multiple times . you need to write a program which replace 
this word with ###### by updating same file.'''


################################################################################
with open("donkey.txt",'r') as f:
    u = f.read()
u = u.replace('donkey','######')
with open("donkey.txt",'w') as f:
     f.write(u)

              

