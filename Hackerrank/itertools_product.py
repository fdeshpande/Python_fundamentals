from itertools import product
p = input().replace(' ',',')
p_ = input().replace(' ',',')
inp= eval(p)
inp_ = eval(p_)
A= []
B = []
B=[]
C=[]
for i in inp:
    A.append(int(i))
for j in inp_:
    B.append(int(j))
# print(A,B)
C.append(A)
C.append(B)
# print(C)
for i in list(product(*C)):
    print(i ,end=' ')

# input :  1 2
#          3 4