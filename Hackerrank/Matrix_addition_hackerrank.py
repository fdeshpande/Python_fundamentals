
print("WELCOME TO MATRIX ADDITION PLATFORM")

row = int(input("Enter the number of rows for matrix : "))
col = int(input("Enter the number of columns for matrix : "))
print(f"Your matrix will be {row}X{col} matrix")
print()
print("Enter the entries row wise :")
matrix_1=[]
for i in range(row):
    a = []
    for j in range(col):
        j = int(input())
        a.append(j)
    print()
    matrix_1.append(a)

for l in range(row):
    for m in range(col):
        print(matrix_1[l][m],end=' ')
    print()

row = int(input("Enter the number of rows for matrix2 : "))
col = int(input("Enter the number of columns for matrix2 : "))
print(f"Your matrix will be {row}X{col} matrix")
print()
print("Enter the entries row wise :")
matrix_2=[]
for i in range(row):
    a = []
    for j in range(col):
        j = int(input())
        a.append(j)
    print()
    matrix_2.append(a)

for l in range(row):
    for m in range(col):
        print(matrix_2[l][m],end=' ')
    print()

print(f"The addition of two matrix is : ")

mat = matrix_1 + matrix_2
for l in mat:
    for m in l:
        print(m)








