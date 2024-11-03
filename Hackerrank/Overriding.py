# # Overriding in multiple inheritance .
#
# class parent1:
#     a=10
#     b=20
#
# class parent2:
#     c=40
#     d=78
#
# class child(parent1,parent2):
#     a=30.40
#     d=45.67
#
# c1 = child()
# print(c1.c)
# print(c1.a)
# print(c1.b)
# print(c1.d)



# Chaining Method :

# class whatsapp:
#     def chats(self):
#         print("only text")
#
# class whatsapp2(whatsapp):
#     def chats(self):
#         super().chats()
#         print("only emojis")
#
# w2 = whatsapp2()
# w2.chats()


# Constructor Chaining:
#
# class parent:
#     def __init__(self):
#         print("I am constructor")
#
# class child(parent):
#     def __init__(self):
#         super().__init__()
#         print("I am another constructor and this is constructor overriding")
#
# c = child()
#
#
# # Constructor chaining with parameters:
#
# class parent:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#
#     def display(self):
#         print(f"first name : {self.fname}")
#         print(f"last name : {self.lname}")
#
# class child(parent):
#     def __init__(self,fname,lname,sal):
#         self.sal=sal
#         super().__init__(fname,lname)
#
#     def demo(self):
#         print(f"salary: {self.sal}")
#         print(f"First name : {self.fname}")
#         print(f"Last name : {self.lname}")
#
# o = child('Falguni','Deshpande',20000)
# o.demo()
# #
