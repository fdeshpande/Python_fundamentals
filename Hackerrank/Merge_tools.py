string= "AAAABBABC"
k=3
a=[]
a.append(string[:k])
a.append(string[k+1:k*2+1])
a.append(string[:-4:-1])
l=[]
str_=''
for i in a:
    for j in i:
        if j not in str_:
            str_ = str_ +j
    l.append(str_)
print(l)

print(5*[0]+5*[10])