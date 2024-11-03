from itertools import permutations
inp = input().split()
print(inp)
l=sorted(list(permutations(inp[0],int(inp[1]))))
for i in l:
    for j in i:
        print(j,end='')
    print()

# input: HACK 2