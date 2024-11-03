from collections import defaultdict

a1, a2 = map(int, input().split())

A = []
B = []

for _ in range(a1):
    a = input()
    A.append(a)

for _ in range(a2):
    b = input()
    B.append(b)

d = defaultdict(list)

for pos, ch in enumerate(A, start=1):
    d[ch].append(pos)

for ch in B:
    positions = d.get(ch, [])
    if positions:
        print(*positions)
    else:
        print("-1")
