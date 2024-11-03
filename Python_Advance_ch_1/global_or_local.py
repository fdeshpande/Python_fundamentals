'''Global keyword is used to modify the variable outside of the current scope...'''

from re import A


a = 54   #global variable
def func():
    global a  # global keyword pre the variable acts as global variable...and use anywhere inthe program.
    print(a)
    a = 8      #local variable which is useful only in  respective function.
    print(a)

func()
print(a)
