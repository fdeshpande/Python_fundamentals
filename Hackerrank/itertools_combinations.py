from itertools import combinations

inp_ = input()
inp = inp_.split()

for f in range(1,int(inp[1])+1):
    combs = sorted(list(combinations(sorted(list(inp[0])), f)))
    # print(combs)

    for c in combs:
        for char in c:
            print(char, end='')
        print()

# input: HACK 2

