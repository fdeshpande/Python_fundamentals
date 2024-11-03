'''We can raise custom exception using the raise keyword in python...'''

def increament(num):
    try:
        num = num + 1
    except:
        raise ValueError("This is not good...") 

a = increament('num')
print(a)
