# n = int(input("Enter any integer : "))
# l = []
# for i in range(n):
#     l.append(i)
#
# for i in l:
#     if i<n:
#         print(i**2)

import math

n = int(input("Enter any num :" ))
l = []
n1 = 0
n2 = 1

print(n1)
print(n2)
for i in range(2,n):
    fibo = n1+n2
    l.append(fibo)
    n1,n2=n2,fibo

for i in l:
    print(i**3)









