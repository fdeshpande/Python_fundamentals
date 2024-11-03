# 2. Question: Check if a Number is Prime

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            return False
    return True

# list the prime numbers in given range
def prime_numbers_in_range(n):
    for i in range(n):
        status = is_prime(i)
        if status == True:
            print(i,end=" ")

# range_ = int(input("Enter range : "))
# prime_numbers_in_range(range_)

# Problem: Write a Python program to print the Fibonacci sequence up to a specified number of terms.

def fibbonacci_series(n):
    a,b=0,1
    for i in range(n):
        print(a, end=" ")
        a,b = b,a+b
# fibbonacci_series(10)

# Problem: Write a Python program to reverse a string without using built-in functions.

def reverse_str(st):
    res_st=""
    for i in st:
        res_st = i+res_st
    return  res_st
# reverse_str("varun")

# Problem: Write a Python program to find the factorial of a number using recursion.
def factorial(n):
    if n<=0 or n<=1:
        return 1
    else:
        return n * factorial(n-1)
# print(factorial(5))

# Problem: Write a Python program to count the number of vowels in a string.
def count_vowels(str):
    c=0
    for i in str:
        if i in "aeiouAEIOU":
            c+=1
    return c
# print(count_vowels("deshpande"))

# Problem: Write a Python program to remove duplicates from a list.

def duplicate_remove_frm_list(lst):
    s = list(set(lst))
    return s
# print(duplicate_remove_frm_list([56,34,6,1,2,3,4,5,6,7,88,9,8,7,7,5,0,9]))

# Problem: Write a Python program to check if a given string is a palindrome.
def is_palindrome(str):
    rev = reverse_str(str)
    if str == rev:
        return True
    else:
        return False

# print(is_palindrome("malayalam"))

# Problem: Write a Python program to find the largest element in a list.
def largest_ele(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] <= lst[j]:
                lst[i],lst[j]=lst[j],lst[i]
    return lst,lst[0]
# print(largest_ele([56,34,6,1,2,3,4,5,6,7,88,9,8,7,7,5,0,9]))

# Problem: Write a Python program to find the sum of digits of a number.
def sum_of_digits(n:int):
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
                lst[i],lst[j]=lst[j],lst[i]
    return lst,f"The second largest number is : {lst[1]}"
# print(second_largest_num([56,34,6,1,2,3,4,5,6,7,88,9,8,7,7,5,0,9])[1])

# Problem: Write a Python program to merge two sorted lists into a single sorted list.
def sort_the_sorted_lst(list1,list2):
    lst=list()
    lst.extend(list1)
    lst.extend(list2)
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] > lst[j]:
                lst[i],lst[j] = lst[j],lst[i]
    return lst
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
# print(sort_the_sorted_lst(list1,list2))

# Problem: Write a Python program to count the number of occurrences of each character in a string.
from collections import defaultdict
from collections import Counter
def count_occurance_character(str):
    # d=defaultdict(int)
    # for i in str:
    #     d[i]+=1
    # d = Counter(str)
    d={}
    # for i in str:
    #     d[i] = str.count(i)
    for i in str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d
# print(count_occurance_character("malayalam"))

# Problem: Write a Python program to find the Greatest Common Divisor (GCD) of two numbers using recursion.
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(a,a%b)
# print(gcd(9,2))

# Problem: Write a Python program to find the intersection of two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
def intersection_lists(lst1,lst2):
    res = set(lst1).intersection(set(lst2))
    return list(res)
# print(intersection_lists(list1,list2))

# Problem: Write a Python program to rotate a list by N positions.
def rotate_list(lst,n):
    a = lst[n::] + lst[:n:]
    return a
# print(rotate_list([1, 2, 3, 4, 5],2))

# Problem: Write a Python program to check if two strings are anagrams of each other.
def anagram(str1,str2):
    if sorted(str1) == sorted(str2):
        return f"'{str1}' and '{str2}' are anagrams"
    else:
        return f"'{str1}' and '{str2}' are not anagrams"

# print(anagram("listen","silent"))

# Problem: Write a Python program to remove all occurrences of a specific element from a list.
def remove_occurance_of_list(lst,ele):
    return [i for i in lst if i != ele]
# print(remove_occurance_of_list([1,2,3,4,5,2,2,5,2,5,2,7,8,9,2,2,2,2],2))

# Problem: Write a Python program to find the longest word in a sentence.
def find_the_longest_word(sentense):
    l = sentense.split(' ')
    # d = {i:len(i) for i in l}
    # f = lambda x: x[1]
    # s = sorted(d,key=f)
    s = sorted(l,key=lambda x:len(x),reverse=True)
    return s[0]
# print(find_the_longest_word("List after removing all occurrences"))

# Problem: Write a Python program to convert a list of tuples into a dictionary.
def list_of_tuples_into_dict(l):
    d = dict(l)
    return d
# print(list_of_tuples_into_dict([(1, 'a'), (2, 'b'), (3, 'c')]))

# Problem: Write a Python program to count the frequency of each word in a sentence.
def frequency(sen):
    d = Counter(sen.split(" "))
    return d
sen = "Python is easy to learn and Python is powerful"
# print(frequency(sen))

# Problem: Write a Python program to find the sum of elements in a list using recursion.
def sum_(list_):
    if not list_:
        return 0
    return list_[0]+sum_(list_[1::])
# print(sum_([1, 2, 3, 4, 5]))

# Problem: Write a Python program to check if a number is a perfect number (i.e., a number that is equal to the sum of its divisors excluding itself).
def perfect_sqr(n):
    divisors_sum = sum([i for i in range(1, n) if n % i == 0])
    return divisors_sum == n
    # l=[]
    # for i in range(1,n):
    #     if i%2==0:
    #         l.append(i)
    #     else:
    #         pass
    # a = sum(l)
    # return a == n

# print(perfect_sqr(25))

# Problem: Write a Python program to find the common elements between two lists without using built-in set operations.
def common_elements(list1, list2):
    l=[]
    for i in list1:
        for j in list2:
            if i==j:
                l.append(i)

    return l
# print(common_elements([1, 2, 3, 4, 5],[4, 5, 6, 7, 8]))

# Problem: Write a Python program to reverse the words in a sentence.
def reverse_the_words(sen):
    l = sen.split(" ")
    res=""
    for i in l:
        res = i +" "+res
    return res

# print(reverse_the_words("Python is amazing for sure and you will enjoy it "))

# def is_prime(n):
#     if n<= 1:
#         return False
#     for i in range(2,int(n ** 0.5)+1):
#         if n % i ==0:
#             return False
#     return True
# print(is_prime(4))

# def factorial(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))

# def fibbonacci(n):
#     a,b=0,1
#     for i in range(n):
#         print(a,end=" ")
#         a,b = b,a+b
# fibbonacci(5)

# sort list of dict

d = [{"name":"Falguni","sal":20000},
     {"name":"Raghu","sal":20500},
     {"name":"Ram","sal":67000},
     {"name":"Shyam","sal":40000}
     ]

# res = sorted(d,key=lambda x:x["sal"],reverse=True)
# print(res)