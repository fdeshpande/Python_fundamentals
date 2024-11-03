s = input("Enter any string : ")

def alphanum_(s):
    alnum_ = [i.isalnum() for i in s]
    print(any(alnum_))

def alphabet_(s):
    alpha_ = [i.isalpha() for i in s]
    print(any(alpha_))

def digit_(s):
    digi_ = [i.isdigit() for i in s]
    print(any(digi_))

def lower_(s):
    low_ = [i.islower() for i in s]
    print(any(low_))

def upper_(s):
    upp_ = [i.isupper() for i in s]
    print(any(upp_))

alphanum_(s)
alphabet_(s)
digit_(s)
lower_(s)
upper_(s)

