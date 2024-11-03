'''Store a multiplication table generated in problem 3 in a file name Tables.txt...'''

a = int(input("Enter any number :\t"))
l = [a*i for i in range(1,11) ]
print(l)
with open('tables.txt','a') as f:
    print(f.write(str(l)))
    f.write("\n")