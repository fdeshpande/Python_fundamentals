'''write a program to mine a log file anf find out whether it contains 'python' '''

with open('log.txt') as f:
    u =f.read().lower()
if 'python' in u:
     print("python is present")
else:
    print("python is not present")     