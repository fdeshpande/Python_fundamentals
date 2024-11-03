vowel = 'aeiouAEIOU'
small = 'abcdefghijklmnopqrstuvwxyz'
capital='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s=('c')
d={}
for i in vowel:
    try:
        ind = small.index(i)
        d[i]=ind
    except:
        ind = capital.index(i)
        d[i] = ind
print(d)
l=[]
if s in vowel:
    print(f"entered char is vowel {s}")
else:
    if s.islower():
        ind1 = small.index(s)
        for k,v in d.items():
            if k.islower():
                if ind1 - v <=5:
                    l.append(v)
        ind_=min(l)
        vowel = small[ind_]
        print(f"smallest char for {s} is {vowel}")
    else:
        ind1 = capital.index(s)
        for k, v in d.items():
            if k.isupper():
                if ind1 - v <= 5:
                    l.append(v)
        ind_ = min(l)
        vowel = capital[ind_]
        print(f"smallest char for {s} is {vowel}")



