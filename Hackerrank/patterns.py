# input =>  s=[[1,2,3],(1,2,3),"hello",{'a':1,'b':2}]
# o/p  =>   {'list': [1, 2, 3], 'tuple': (1, 2, 3), 'string': 'hello', 'dictionary': {'a': 1, 'b': 2}}

# s=[[1,2,3],(1,2,3),"hello",{'a':1,'b':2}]
#
# d={}
# for i in s:
#     if isinstance(i,str):
#         d['string'] = i
#     if isinstance(i,list):
#         d['list'] = i
#     if isinstance(i,tuple):
#         d['tuple'] = i
#     if isinstance(i,dict):
#         d['dictionary'] = i
# print(d)
#
# # input =>  reverse the string without typecasting.
# num = 123456789
# rev = 0
# while(num>0):
#     a = num % 10
#     rev = rev * 10 +a
#     num = num // 10
# print(rev)


# inp = int(input())
# l=len(bin(inp)[2:])
# for i in range(inp+1):
#     hexx = str(hex(i)).replace('0x', '')
#     if hexx.isalpha():
#         hexx = hexx.capitalize()
#     if hexx.isalnum():
#         hexx=hexx.title()
#     print(str(int(i)).rjust(l), str(oct(i)).replace('0o', '').rjust(l), hexx.rjust(l), str(bin(i)).replace('0b', '').rjust(l))

# s= 'Sample'
# s='Z'+s[1:]
# print(s)




#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust((thickness-1),' ')+c+(c*i).ljust((thickness-1),' '))

# #Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2,' ')+(c*thickness).center(thickness*6,' '))

# #Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center((thickness*6),' '))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2,' ')+(c*thickness).center(thickness*6,' '))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust((thickness),' ')+c+(c*(thickness-i-1)).ljust((thickness),' ')).rjust(thickness*6,' '))









