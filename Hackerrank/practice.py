# num = int(input("enter any number : "))
# for i in range(0,num+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#
#     print("\n")
#
#
# print()
#
# n=4
# for i in range(n,0,-1):
#     print("* "*i)
#
#
# # WAP to get number1 is greater than num2 and 3 but nor 4
# n1 = 74
# n2 = 65
# n3 = 34
# n4 = 77
#
# if n1>n2 and n1>n3 and not n1>n4:
#     print(n1)
#
# # WAP to check if the given char is lower case or not and check a character is digit or special character:
# c = input("enter character : ")
# # if ord(c)>=97 and ord(c)<=122:
# if c.islower():
#     print(f"{c} is lower case and upper case of this char is {chr(ord(c)-32)}")
# # elif ord(c)>65 and ord(c)<90:
# elif c.isupper():
#     print(f"{c} is upper case and lower case of this char is {chr(ord(c)+32)}")
# # elif ord(c)>=48 and ord(c)<=57:
# elif c.isdigit():
#     print(f"{c} is digit")
# else:
#     print(f"{c} is special character.")
#
# # WAP to get second largest number among three numbers:
#
# a,b,c= 65,45,87
#
# if a>b and a>c:
#     if b>c:
#         print(f"{b} is second largest")
#     else:
#         print(f"{c} is second largest")
# elif b>a and b>c:
#     if a>c:
#         print(f"{a} is second largest")
#     else:
#         print(f"{c} is second largest")
# else:
#     if a>b:
#         print(f"{a} is second largest")
#     else:
#         print(f"{b} is second largest")
#
# l = [a,b,c]
# # l.sort
# l1=sorted(l)
# print(l1[1])
#
# WAP to check whether the num is prime or not
#
# def is_prime_div2(num):
#     if num <=1:
#         return False
#     for i in range(2,num//2 + 1):
#         if num % i ==0:
#             return False
#     else:
#         return True
#
# # number = int(input("Enter a number: "))
# for number in range(10):
#     if is_prime_div2(number):
#         print(f"{number} is a prime number.")
#     else:
#         pass
#         # print(f"{number} is not a prime number.")
#
# WAP to find leap yr or not
#
# def leapyr(year):
#     if year % 400 ==0 and year % 4 ==0 or year%100 != 0:
#         print(f"{year} is leap year" )
#     else:
#         print(f"{year} not a leap yr")
#
# leapyr(1996)
#
#  WAP to check number of keys in dictionary if the number of keys in dictionary even print the number of keys as it is
# else add one in it.
#
# d={"a":1,"b":2,"c":3}
# if len(d) % 2 == 0:
#     print(d)
# else:
#     d["d"]=4
#     print(d)
#
# s = "kjtydcuYk"
# res= ""
# l=len(s)
# for i in range(l-1,-1,-1):
#     res=res+s[i]
# if s == res:
#     print(f"{s} is palindrome")
# else:
#     print(f"{s} is not palindrome")
#
# WAP to print first chrs of elem without using slicing.
#
# l =["google","apple","microsoft","walmart","flipkart","amazon","facebook"]
# n = int(input("Enter number :"))
# s=""
# for i in l:
#     for j in range(len(i)):
#         if j<n:
#             print(i[j],end="")
#         else:
#             break
#     print()
#
# WAP to create dict and how many times ch is present.
# s = "hellolll python"
# d={}
# # print(type(d))
# for i in s:
#     if i not in d:
#         d[i] = s.count(i)
#     else:
#         pass
# print(d)
#
# WAP to count a word in lst
# l ="google apple microsoft walmart flipkart amazon facebook"
# print(len(l.split()))
#
# WAP to print repetative ch in str
# c = 0
# for i in l:
#     if l.count(i) >1:
#         print(i,l.count(i))
#
# # WAP to print words starting with vowels
# l ="google apple microsoft walmart flipkart amazon facebook"
# for i in l.split(" "):
#     if i[0] in "aeiouAEIOU":
#         print(i)
#
# # WAP to create a list of even length words
# l ="google apple microsoft walmart flipkart amazon facebook"
# ll=[]
# for i in l.split(" "):
#     if len(i)%2==0:
#         ll.append(i)
# print(ll)
#
# # WAP to create a list of words ending with vowel
# l ="google apple microsoft walmart flipkart amazon facebook"
# l2=[]
# for i in l.split(" "):
#     if i[-1] in "aeiouAEIOU":
#         l2.append(i)
# print(l2)
#
# # WAP to create a list of tuples with words and its length pair
# l ="google apple microsoft walmart flipkart amazon facebook"
# l3=[]
# for i in l.split(" "):
#     l3.append((i,len(i)))
# print(l3)
#
# # WAP to create a dict wih words and its length pair starting with vowels
# l ="google apple microsoft walmart flipkart amazon facebook"
# d={}
# for i in l.split(" "):
#     if i[0] in "aeiouAEIOU":
#         d[i] = len(i)
# print(d)
#
# # WAP to create a dict wih words and its length pair ending with vowels
# l ="google apple microsoft walmart flipkart amazon facebook"
# d={}
# for i in l.split(" "):
#     if i[-1] in "aeiouAEIOU":
#         d[i] = len(i)
# print(d)
#
# # WAP to create a dict with letter words starting with that letter.
# l ="google apple microsoft walmart flipkart amazon facebook"
# d1={}
# for i in l.split(" "):
#     d1[i[0]] = i
# print(d1)
#
# # WAP to create a dict of ch and its indices pair
# l ="google apple microsoft walmart flipkart amazon facebook"
# d={}
# for i in l.split(" "):
#     d[i] = l.split(" ").index(i)
# print(d)
#
# # WAP to create a dict of ch and its ascii value pair
# l ="google apple microsoft walmart flipkart amazon facebook 45 78 98"
# d={}
# for i in l:
#     if i not in d:
#         d[i] = ord(i)
#     else:
#         pass
# print(d)
#
# # WAP to create a dict with value of numeric datatype
# l ="google apple microsoft walmart flipkart amazon facebook 45 78 98"
# d={}
# for i in l.split(" "):
#     if i.isdigit():
#         d[i] = i
# print(d)
#
# # WAP to create a dict if the value is of str datatype reverse it else keep it as it is.
# l ="google apple microsoft walmart flipkart amazon facebook 45 78 98"
# d={}
# for i in l.split(" "):
#     if i.isdigit():
#         d[i] = i
#     else:
#         d[i] = i[::-1]
# print(d)
#
# # WAP to reverse a string/tuple/list
# s= "hello world"
# print(s[::-1])
#
# s1=""
# for i in range(len(s)-1,-1,-1):
#     s1= s1+s[i]
# print(s1)
#
# s2 = str(list(reversed(s))).replace(",","").replace("[","").replace("]","").replace("'","").replace(" ","",)
# print(s2)
#
# # WAP to print indexes and value
# s= "hello world"
# for i,j in enumerate(s,start=1):
#     print(i,j,sep=":",end=" ")
# # WAP to take ele from list1 and tuple1 make it as dict of ele from making key as list and value as tuple
# l=['a','b','c','d','e']
# t=[111,222,333,444,555,666]
# l2=['apple','bag','cat','dog']
#
# for i in zip(l,t):
#     print(i)
#
# from itertools import zip_longest
# for i in zip_longest(l,l2):
#     print(i)
#
# list comprehenstion
# WAP to create list comprehenstion in which str of even lenth keep it as is it is else reversse it.
# l ="google apple microsoft walmart flipkart amazon facebook 45 78 958"
# l1 = [i if len(i)%2==0  else i[::-1] for i in l.split(" ")]
# print(l1)
#
# l=[print(i,"even") for i in range(10) if i%2==0]
#
# # WAP to create a dict if the value is of str datatype reverse it else keep it as it is.
# l ="google apple microsoft walmart flipkart amazon facebook 45 78 98"
# d={}
# for i in l.split(" "):
#     if i.isdigit():
#         d[i] = i
#     else:
#         d[i] = i[::-1]
#
# d = {i if i.isdigit() else i:i[::-1] for i in l.split(" ")}
# print(d)
#
# d_={'g': 103, 'o': 111, 'l': 108, 'e': 101, ' ': 32, 'a': 97, 'p': 112, 'm': 109, 'i': 105}
# d = {j:i for i,j in d_.items()}
# print(d)
#
# default dict
# WAP to grouping flowers and animals in below list.
# items= ['lotus-flower','lilly-flower','cat-animal','rose-flower','lion-animal']
# from collections import defaultdict
# d = defaultdict(list)
# for ch in items:
#     a = ch.split("-")
#     # print(a)
#     v,k=a
#     d[k]+=[v]
# print(d)
#
# # WAP to group even and odd numvber
# n = [1,2,3,4,5,6,7,8,9,10]
# dd=defaultdict(list)
# for i in n:
#     res = i%2==0
#     if res == 0:
#         dd["odd"] += [i]
#     else:
#         dd["even"] += [i]
# print(dd)
#
# d = defaultdict(list)
# for i,j in enumerate(n):
#     d[i] += [j]
# print(d)
#
# Write a recurssion function to print the number from 1 to 20
# def call_(number=1):
#     if number>20:
#         return
#     print(number)
#     number+=1
#     call_(number)
# call_()
#
# WAP num from 0 to n
# def numbers_(n,i=0):
#     if i>n:
#         return
#     print(i)
#     i+=1
#     numbers_(n,i)
# numbers_(17)
#
# WAP return factorial of num
#
# def factorial(n,fact=1,i=1):
#     if i>n:
#         return fact
#     fact *= i
#     i+=1
#     return factorial(n,fact,i)
#
# print(factorial(7))
#
# WAP to return sum of numbers from 0 to n
#
# def sum_(n,sum=0,i=0):
#     if i>n:
#         return sum
#     sum += i
#     i +=1
#     return sum_(n,sum,i)
# print(sum_(7))
# l=[1,2,3,4,5,6,7,8]
# l_=l[:3]
# l__ = l[3:]
# l=l_+[5]+l__
# print(l)
def insert_(lst,pos,ele):
    if isinstance(lst,(list)):
        l = []
        if pos > len(lst):
            return f"entered {pos} is out of list range"
        elif pos+1 < len(lst):
            l += lst[:pos]
            l += [ele]
            l += lst[pos:]
            return l
        elif pos == len(lst):
            l = lst+[ele]
            return l
        else:
            return f'{type(lst)}  has no attributes called insert'

print(insert_([1,2,3,4,5,6],2,'hi'))
#
# Lambda function
#
# a = lambda n,m: n+m
# print(a(10,20))
#
# a = lambda x: x**2 if x%2==0 else x**3
# print(a(109))
#
# l = [{"emp_no":101,"name":"Ram","salary":25000},
#      {"emp_no":103,"name":"Sham","salary":20000},
#      {"emp_no":105,"name":"Pritam","salary":55000},
#      {"emp_no":106,"name":"Aman","salary":50000},
#      {"emp_no":109,"name":"Raman","salary":30000}]
#
# print(sorted(l,key=lambda x: x["salary"],reverse= False))
#

# MAP()
# WAP to check odd and even number in the list using map.
# l= list(range(10))
# even_odd = lambda x: f"{x} is even" if x % 2 ==0 else f"{x} is odd"
# res= list(map(even_odd,l))
# print(res)
#
# # WAP to check if the str is palindrome or not
# l1=["madam","mom","python","level","hello"]
# palin = lambda x: f"{x} is palindrome" if x == x[::-1] else f"{x} is not palindrome"
# res = list(map(palin,l1))
# print(res)

# WAP to convert str in uppercase present in lsit
# l1=["madam","mom","python","level","hello"]
# case = lambda x: x.upper()
# res = list(map(case,l1))
# print(res)

# WAP to convert -ve num into +ve num present in lst
# l2=[-5,-6,9,-34,90,-38,78,-100]
# print(list(map(abs,l2)))

# WAP to return word and its length pair of ele of list
# s="hey guys good morning welcome to the python session"
# a = lambda x: (x,len(x))
# res = list(map(a,s.split(" ")))
# print(res)

# WAP to add ele in two lst
# l=[2,4,6,8,10]
# ll=[1,3,5,7,9]
# a = lambda x : x[0]+x[1]
# res = list(map(a,zip(l,ll)))
# print(res)

# WAP to raise the power of number with their indices
# l=[3,6,2,4,7]
# a = lambda x: x[1]**x[0]
# res = list(map(a,enumerate(l)))
# print(res)

# WAP to return list of having square of the elements present in the list
# l=[2,4,6,8,10]
# a = lambda x: x**2
# res = list(map(a,l))
# print(res)

# WAP to return dictionary of word and reversed word pair
# l=["apple","instagram","python","level","hello"]
# a = lambda x: {x:x[::-1]}
# res = list(map(a,l))
# print(res)

# WAP to return a tuple having nested tuples of two elems and that should be dividing a word into two elems equally.
# l=["apple","instagram","python","level","hello"]
# a = lambda x: (x[:len(x)//2],x[len(x)//2::])
# res = list(map(a,l))
# print(res)

# Filter
# WAP to filter only even numbers
# l=[1,2,3,4,5,6,7,8,9]
# a = lambda x: x if x%2==0 else False
# res  = list(filter(a,l))
# print(res)

# WAP to filter the list elems whos lenght is >5
# l=["apple","instagram","python","level","hello"]
# a = lambda x: x if len(x)>5 else False
# res  = list(filter(a,l))
# print(res)

# WAP to build a lst with only even length strngs using filter
# names = ["apple","google","walmart","fb","insta","act","acne","zomato","hp"]
# a = lambda x: x if len(x)%2==0 else False
# res  = list(filter(a,names))
# print(res)

# WAP to return a string if the string starting with vowels
# names = ["apple","google","walmart","fb","insta","act","acne","zomato","hp"]
# a = lambda x: x if x[0] in "aeiouAEIOU" else False
# res  = list(filter(a,names))
# print(res)

# WAP to return a lst having flowers
# l=["sun flower","mari gold","lotus flower","rose flower","banana tree"]
# a = lambda x: x if "flower" in x.split(" ") else False
# res  = list(filter(a,l))
# print(res)

# Pandas
# import pandas
# import pandas as pd
#
# name = ['sun flower', 'lotus flower', 'rose flower']
# age = [21,22,23]
# gender = ["Male","Female","Female"]
#
# df = pd.DataFrame({"name":name,"age":age,"gender":gender})
# print(df)
#
# d = {"name":['sun flower', 'lotus flower', 'rose flower'],"age":[21,22,23],"gender":["Male","Female","Female"]}
# df1 = pd.DataFrame(d)
# print(df1)
#
# df1["dept"] = ["electric engineer","IT engineer","IOT engineer"]
# print(df1["name"].values)

# Decorators
# WADF to check number of students attending classes
# def outer(func):
#     def inner(*args,**kwargs):
#         for i in args:
#             print(i)
#         print("function name", func.__name__)
#         print("The total number of students are",end=" ")
#
#         func(*args,**kwargs)
#     return inner
#
# @outer
# def student(g,b):
#     c = g+b
#     print(c)
# student(70,76)
#
# import time
# def exe_time(func):
#     def inner(*args,**kwargs):
#         start = time.time()
#         func(*args,**kwargs)
#         end = time.time()
#
#         return "The total time is ",end-start
#     return inner
#
# @exe_time
# def add_():
#     for i in list(range(10)):
#         time.sleep(1)
#         print(i)
# print(add_())
#

#File Handling
# import csv
# import os
#
# with open("","w",newline=" ") as file:
#     a = csv.writer(file)
#     a.writerow([])
#     a.writerows([{}])
#
# os.popen()
# with open("","w",newline=" ") as file:
#     a = csv.DictWriter(file,["A","B","C"])
#     a.writeheader()
#     a.writerows([{}])
#
# os.popen()


# OOP

# class A:
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#
# a = A("Radha","Kishori")
# print(a.fname)
# print(a.lname)
# print(a.__dict__)
#
#
# class B:
#     def name(self,fname,lname):
#         self.fname = fname
#         self.lname= lname
#
# b = B()
# b.name("Jaya","Sushma")
# print(b.fname,b.lname)


# class A:
#     a="I am A class and Parent class"
#
# class B(A):
#     b= "I am B class"
#     print(A.a)
#     print("I am B class and inherits A class single level")
#
# class C(B):
#     c = "I am C class"
#     print(B.b)
#     print(A.a)
#     print("I am C class and inherits A and B class multilevel")
#
# class E:
#     e = "I am e class"
# class D(A,E):
#     d = "I am D class"
#     print(A.a)
#     print(E.e)
#     print("I am D class and inherits A,E class multiple level")
#
#
# d = D()
# print(d)

# Overriding in multiple inheritance




# 2. Question: Check if a Number is Prime
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

# list the prime numbers in given range
def prime_numbers_in_range(range_):
    for i in range(range_):
        if is_prime(i):
            print(i)
        else:
            pass

# range_ = int(input("Enter range : "))
# prime_numbers_in_range(range_)

# Problem: Write a Python program to print the Fibonacci sequence up to a specified number of terms.
def fibbonacci(n):
    a,b = 0,1
    for i in range(n):
        print(a,end=" ")
        a,b = b,a+b

fibbonacci(7)
# Problem: Write a Python program to reverse a string without using built-in functions.

def revstr(strr):
    st = ""
    for i in strr:
        st = i + st
    return st
# print(revstr("varun"))

# Problem: Write a Python program to find the factorial of a number using recursion.
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
# print(factorial(5))

# Problem: Write a Python program to count the number of vowels in a string.
def vowel_in_str(str):
    c=0
    for i in str:
        if i in "aeiouAEIOU":
            c += 1
    return c
# print(vowel_in_str("varun"))

# Problem: Write a Python program to remove duplicates from a list.
def duplicate_remove_frm_list(lst):
    l=[]
    for i in lst:
        if i not in l:
            l.append(i)
    lst.clear()
    lst = l
    return lst
# print(duplicate_remove_frm_list([56,34,6,1,2,3,4,5,6,7,88,9,8,7,7,5,0,9]))

# Problem: Write a Python program to check if a given string is a palindrome.
def is_palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False
# print(is_palindrome("malayalam"))

# Problem: Write a Python program to find the largest element in a list.
def largest_ele(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]<lst[j]:
                temp = lst[i]
                lst[i]=lst[j]
                lst[j]=temp
    return lst[0]

# print(largest_ele([56,34,6,1,2,3,4,5,6,7,88,9,8,7,7,5,0,9]))

# Problem: Write a Python program to find the sum of digits of a number.
def sum_of_digits(n):
    sum_=0
    while n>0:
        sum_ += n%10
        n //= 10
    return sum_
# print(sum_of_digits(12345))

# Problem: Write a Python program to find the second largest number in a list.
def second_largest_num(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] < lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst[1]
# print(second_largest_num([56,34,6,1,2,3,4,5,6,7,88,9,8,7,7,5,0,9]))

# Problem: Write a Python program to merge two sorted lists into a single sorted list.
list1=[56,34,6,1,2,3,4,5,6,7,88,9,8,7,7,5,0,9]
list2=[56,34,6,1,2,3,4,5,6,7,88,90,45,44,23]
def sort_the_sorted_lst(list1,list2):
    lst_ = []
    lst_.extend(set(list1))
    lst_.extend(set(list2))
    lst_ = sorted(set(lst_))
    return lst_

# print(sort_the_sorted_lst(list1,list2))

# Problem: Write a Python program to count the number of occurrences of each character in a string.
from collections import defaultdict
from collections import Counter
def count_occurance_character(str):
    # d = defaultdict(int)
    # for i in str:
    #     d[i] += 1

    d = Counter(str)
    return d
# print(count_occurance_character("malayalam"))

# Problem: Write a Python program to find the Greatest Common Divisor (GCD) of two numbers using recursion.
def gcd(n1,n2):
    if n2 == 0:
        return n1
    else:
        return gcd(n1,n1%n2)
# print(gcd(9,2))

# Problem: Write a Python program to find the intersection of two lists.
def intersection_lists(l1,l2):
    a = set(l1).intersection(set(l2))
    return a
# print(intersection_lists(list1,list2))

# Problem: Write a Python program to rotate a list by N positions.
def rotate_list(l,n):
    return l[n::]+l[:n:]
# print(rotate_list([1, 2, 3, 4, 5],2))

# Problem: Write a Python program to check if two strings are anagrams of each other.
def anagram(st1,st2):
    if sorted(st1) == sorted(st2):
        print("both are anagrams")
    else:
        print("both are not anagrams")

# anagram("listen","silent")

# Problem: Write a Python program to remove all occurrences of a specific element from a list.
def remove_occurance_of_list(l,n):
    return [i for i in l if i != n]
# print(remove_occurance_of_list([1,2,3,4,5,2,2,5,2,5,2,7,8,9,2,2,2,2],2))

# Problem: Write a Python program to find the longest word in a sentence.
def find_the_longest_word(str):
    l = str.split(' ')
    res = sorted(l,key= lambda x: len(x),reverse=True)[0]
    return res
# print(find_the_longest_word("List after removing all occurrences"))

# Problem: Write a Python program to convert a list of tuples into a dictionary.
def list_of_tuples_into_dict(l):
    d=dict(l)
    return d
# print(list_of_tuples_into_dict([(1, 'a'), (2, 'b'), (3, 'c')]))

# Problem: Write a Python program to count the frequency of each word in a sentence.
def frequency(str):
    d = Counter(str.split(" "))
    return d
# print(frequency("List after removing all occurrences removing all occurrences"))

# Problem: Write a Python program to find the sum of elements in a list using recursion.
def sum_(l):
    if not l:
        return 0
    else:
        return l[0] + sum_(l[1::])
# print(sum_([1, 2, 3, 4, 5]))

# Problem: Write a Python program to check if a number is a perfect number (i.e., a number that is equal to the sum of its divisors excluding itself).
def perfect_sqr(n):
    divisors_sum = sum([i for i in range(1, n) if n % i == 0])
    return divisors_sum == n
# print(perfect_sqr(25))

# Problem: Write a Python program to find the common elements between two lists without using built-in set operations.
def common_elements(l1,l2):
    l=[]
    for i in l1:
        if i in l2:
            l.append(i)
    return l
# print(common_elements([1, 2, 3, 4, 5],[4, 5, 6, 7, 8]))

# Problem: Write a Python program to reverse the words in a sentence.
def reverse_the_words(str):
    res=''
    l = str.split(" ")
    for i in l:
        res +=" "+ i[::-1]
    return res

# print(reverse_the_words("Python is amazing for sure and you will enjoy it "))

# sort list of dict

d = [{"name":"Falguni","sal":20000},
     {"name":"Raghu","sal":20500},
     {"name":"Ram","sal":67000},
     {"name":"Shyam","sal":40000}
     ]
res = sorted(d,key=lambda x: x["sal"])
# print(res)