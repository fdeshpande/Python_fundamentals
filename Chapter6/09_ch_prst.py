'''Write a program to calculate the grade of a student from his marks from the 
following scheme:
                     80 - 100 A
                     60 - 79 B
                     50 - 59 c
                     >50 - D
'''
print("Sincerely mention your total marks out of 100 :")
totalMarks = int(input("Enter your total marks :\t"))
print("your entered Marks are",totalMarks)

if totalMarks >=90:
    grade = 'A'

elif totalMarks >=80:
    grade = 'B'  

elif totalMarks >=70:
    grade = 'C'  

elif totalMarks >=60:
    grade = 'D'      

elif totalMarks >=50:
    grade = 'F' 

print(grade)         





