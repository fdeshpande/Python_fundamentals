A=[{"apple": 5, "orange": 1, "mango": 7, "grapes": 8},{"apple": 4, "orange": 6, "grapes": 1},{"orange": 6, "mango" : 7, "grapes": 8},]
new={}
for i in A:
    for key,value in i.items():
        # print(key,value)
        if key not in new:
            new[key]=value
        else:
            new[key]+=value
print(new)