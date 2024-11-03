'''Write a program to find out whether a student is pass or fail ,
 if it requires total 40% and atleast 33% in each subject to pass .
 assume three subjects and take marks as an input from the user.'''

sub1 = int(input("Enter the marks of maths:\t\n "))
sub2 = int(input("Enter the marks of Science:\t\n "))
sub3 = int(input("Enter the marks of marathi:\t\n "))
subMarks = [sub1 ,sub2 ,sub3]
print(subMarks)

requireMarks = 40
if(sub1>=requireMarks):
    print("Student is passed in maths!!!!")
else:
    print("you are fail in maths. study hard...")

if(sub2>=requireMarks):
    print("Student is passed in Science!!!!")
else:
    print("you are fail in science. study hard...")

if(sub3>=requireMarks):
    print("Student is passed in marathi!!!!")
else:
    print("you are fail in marathi. study hard...")    