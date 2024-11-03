inp = input()
# print(inp)
for i in range(int(inp)):
    inp_ = input().split()
    if inp_[0].isdigit():
        a = int(inp_[0])
    else:
        a = inp_[0]
    if inp_[1].isdigit():
        b = int(inp_[1])
    else:
        b = inp_[1]
    # print(a,b)
    try:
        c = a // b
        # print(c)
    except Exception as e:
        print("Error Code: ",e)

