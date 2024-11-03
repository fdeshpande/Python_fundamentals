'''A list contains a multiplication table of 7 . write a program to convert it to a 
 vertical string of same number(7
                                14)'''

l = [str(i*7) for i in range(1,11)]

sentence = '\n'.join(l) # it will show error because join only joins string instance
print(sentence)