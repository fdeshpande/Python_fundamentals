''' Write a program to filter a list of numbers which are divisible by 5 '''
def Divisible_by_5(num):
    if num%5 == 0:
        return True
    else:
        return False

l = [3,4,5,67,8,90,45,65,60,95]
print(list(filter(Divisible_by_5,l)))
