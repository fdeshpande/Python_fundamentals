'''python offers finally clause which ensures exception of a piece of code irrespective 
of the execution...'''
try:
    a = int(input("Enter a number :\t"))
    c = 1/a
    print(c)

except Exception as e:
    print(e)
    exit()

finally:
    print("We are done!!!")

print("*************************************************************")



