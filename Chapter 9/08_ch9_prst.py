'''Write a program to find out whether a file is identical and matches the content of another file.'''

f1 = 'copy.txt'
f2 = 'this.txt'

with open(f1) as f:
    fa = f.read()

with open(f2) as f:
    fb = f.read()

if fa == fb:
    print("Files are identical...")
else:
    print("Files are not identical...")            