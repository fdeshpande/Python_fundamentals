''' Write a program to input name , marks and phone nmber of a student 
and format it using the format function like below...

"The name of student is Harry . His marks are 7 . His phone number is 9999756022" '''

name = input("Enter student name : \t")
marks = int(input("Enter marks of student :\t"))
ph_no = int(input("Enter his/her phone number:\t"))

b = "The name of student is {0} . His/her marks are {1} . His/her phone number is {2}".format(name,marks,ph_no)
print(b)