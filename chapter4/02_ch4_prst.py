# Write a program to accept marks of 6 students and display them in a sorted manner.

print("Enter the student name and their marks:" )
Ayush = input("Enter the marks of Ayush :\t")
Ritesh = input("Enter the marks of Ritesh :\t")
Vikas = input("Enter the marks of Vikas :\t")
Sameer = input("Enter the marks Sameer :\t")
Shivam = input("Enter the marks of Shivam :\t")
Suprit = input("Enter the marks of Suprit :\t")
markList =[Ayush,Ritesh,Vikas,Sameer,Shivam,Suprit]
print('The unsorted mark list is:\t',markList)
markList.sort()
print('The sorted mark list is:\t',markList)