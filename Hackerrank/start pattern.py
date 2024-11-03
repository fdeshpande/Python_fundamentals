
#for right angle triangle

n = 5

for i in range(0, n):
    for j in range(0, i + 1):
        print("* ", end="")
    print(" ")

#for triangle

n=5
for i in range(1, n + 1):
    for j in range(n, i, -1):
        print(" ", end=" ")
    for k in range(1, 2*i):
        print(" *", end="")
    print()

for i in range(5):
    x='* '
    x=x*i
    print(f'{x: >10}')

st = "dummy"
st_=''
c = 1
for i in st:
    if st.count(i)>1:
            st_=st_+'$'
    else:
        st_=st_+i
print(st_)





